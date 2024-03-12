import java.io.PrintWriter
import scala.sys.process._

@main def exec(cpgFile: String, source: String, sink: String): Unit = {
    importCode(inputPath=cpgFile, projectName="Program")
    val taintSource = cpg.call.name(source)
    val taintSink = cpg.call.name(sink)

    val flows = taintSink.reachableByFlows(taintSource).p
    val flowsType = flows.getClass.getSimpleName
    val flowHead = flows.head
    val lines = flowHead.split("\n")
    var lineList = lines.toList
    lineList = lineList.drop(4)
    lineList = lineList.init

    // Write DOT representation to a file
    val writer = new PrintWriter("output.dot")
    writer.println("digraph flowGraph {")
    writer.println("\tStart -> " + s""""${escapeQuotes(lineList.head)}"""" + ";") // Adding start node
    lineList.zipWithIndex.foreach { case (element, index) =>
        val currentNode = s""""${escapeQuotes(element)}""""
        val nextNode = if (index + 1 < lineList.size) s""""${escapeQuotes(lineList(index + 1))}"""" else """"Exit""""
        writer.println(s"\t$currentNode -> $nextNode;")
    }
    writer.println("}")
    writer.close()

    
    convertDotToPng("output.dot", "output.png")
}

def escapeQuotes(str: String): String = {
    str.replace("\"", "\\\"")
}

def convertDotToPng(dotFileName: String, pngFileName: String): Unit = {
    val command = s"dot -Tpng $dotFileName -o $pngFileName"
    val exitCode = command.!
    if (exitCode == 0) {
        println(s"Conversion successful: $dotFileName -> $pngFileName")
    } else {
        println(s"Conversion failed for $dotFileName")
    }
}


