<!-- # JoernAnalysis
This project uses Joern data flow analysis tool to track flow of data in the source code. -->


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h1 align="center">Joern Analysis</h3>

  <p align="center">
    This project uses Joern data flow analysis tool to track flow of data in the source code.
    <br />
<!--     <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  </p>
</div>



<!-- GETTING STARTED -->
## Getting Started

This is an example to set up the project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

1. Installation of JDK : This project requires installation of JDK as a prerequisite. The instructions on installation can be found [here](https://docs.oracle.com/en/java/javase/18/install/overview-jdk-installation.html#GUID-8677A77F-231A-40F7-98B9-1FD0B48C346A). Installation of java comes with the JDK, the instruction for installing java are [here](https://www.oracle.com/java/technologies/downloads/).
There are tutorials on youtube which can be helpful to install on [Windows](https://www.youtube.com/watch?v=jPwrWjEwtrw) and [Mac](https://www.youtube.com/watch?v=PQk9O03cukQ).
2. Installation of Joern : Below are the instructions for the installation.




### Installation of Joern

1. Install shell script
   ```sh
   curl -L "https://github.com/joernio/joern/releases/latest/download/joern-install.sh" -o joern-install.sh
   ```
2. Change mode to make file executable
   ```sh
   chmod u+x joern-install.sh
   ```
3. Run the installer
   ```sh
   ./joern-install.sh --interactive
   ```
4. You can test your installation by running the following command
   ```sh
   joern
   ```


### Installation of this project

1. Clone the repo
   ```sh
   git clone https://github.com/TausifAnsari/JoernAnalysis.git
   ```
3. Change directory to project root
   ```sh
   cd JoernAnalysis
   ```
   Note: Would you like to create a symlink to the Joern tools? [y/N]: y
4. Open the project in Visual Studio Code
   ```sh
   code .
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This repository contains two scripts, `flowGraph1.sc` and `flowGraph2.sc`, designed to generate different graphs by analyzing the data flow within source code.

To utilize the scripts provided in this repository, follow these steps:

1. Once you are done cloning the repository, Run the below command with the appropriate parameters.
   ```sh
   joern --script flowGraph1.sc --param cpgFile=./Program1 --param source=input --param sink=print
   ```

   cpgFile: Specify the directory containing the project or source code. <br />
   source: Define the method from which you want to track the flow of data. <br />
   sink: Identify where the data flow ends. If the source meets the sink, a graph will be generated. <br />


### Running the Script on Your Own Code or Project
To run this data flow analysis on other programs you can create a new directory and write program in it and use the script to generate graph.

1. Create a new directory for your program
   ```sh
   mkdir new_program
   ```
2. Move your program files into the newly created directory
   ```sh
   mv /path/to/your/program_files/* new_program/
   ```
3. Run the below command with updated parameters, specifying the new program directory, the source method and the sink method
   ```sh
   joern --script flowGraph1.sc --param cpgFile=./new_program --param source=input --param sink=print
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
