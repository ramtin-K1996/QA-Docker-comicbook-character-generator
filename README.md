QaProject - DOCKER

<h2 align="center">  Comic Book character generator </h2>


![image](https://user-images.githubusercontent.com/104978129/178021102-f7aef2fd-ac08-4d3f-b2f7-0b2ebbaece40.png)


<h3 align="center"> implementation  </h3>

<h5> 
<br> 
Project Developed with, <br><br>

* python flask
* Kanban Board: trello
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
</h5>
<br>
The logic of the application is very simple, every time the user refreshes the page two attributes are chosen at random a power and a publisher. Depending on these two attributes a hero is selected at random from a list. Each character has a different chance of being chosen. 

<br>
<br>
<br>
<br>
<h5 align="center">(Design sample) </h5>
<br>


<img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(261).png" width="500"/> <img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(258).png" width="500"/> 




<img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(259).png" width="500"/> <img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(255).png" width="500"/> 

<h5>
% of being chosen <br><br>

21%  - Green lantern <br>
20% - Mr fantastic <br>
20% - Spider-man <br>
16% - Martian manhunter<br> 
8% - Batman <br>
6% -Ironman<br>
6% - Hulk<br>
4 % -Superman<br> 
</h5>
<br>
<br>
<br>

<b> TRELLO </b>
<br>
![image](https://user-images.githubusercontent.com/104978129/178032903-d20a75d3-9293-48c1-8217-b8ae069444ec.png)

<br>
<br>
<b> reverse proxy implementation </b>

![image](https://user-images.githubusercontent.com/104978129/178031196-aa390bbb-810d-49fa-b245-81a8bde7e904.png)

<br>
<br>
<b> risk assessment </b>

![image](https://user-images.githubusercontent.com/104978129/178034297-9e04fc97-18c0-48cb-b172-0f5695f0844b.png)

<br>
<br>
<br>
<b> unit testing</b>
<br>
each service was tested with coverage. since each test is located within the service i wrote a script that automate testing of each service. <br>

![image](https://user-images.githubusercontent.com/104978129/178036116-44a9718d-3729-4853-8d9d-94965f79aa93.png)
<br>
<br>
<img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(243).png" width="500"/> <img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(242).png" width="500"/> 
<br>
<img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(244).png" width="500"/> <img src="https://github.com/ramtin-K1996/QA-Docker-comicbook-character-generator/blob/main/screenshots/Screenshot%20(245).png" width="500"/> 
<br>
<br>
<b> analysis </b>

In terms of improvements the project was more intended for display of codependency with the implementation tools rather than the python application. Nonetheless I would have liked to improve upon the simplicity of the applications logic. Currently there is only eight possible outcomes I would have liked to ideally expand on that,  Some of the code implementation I would have changed or tidied up. Ultimately time constraints were the deciding factor. 
