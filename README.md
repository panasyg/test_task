Для того аби підняти наш сервер:
- стягуємо образ з мого DockerHub( https://hub.docker.com/r/panasyg/softwarenetictask ) 
![image](https://user-images.githubusercontent.com/91308486/180341170-2951d924-0966-4a3f-8d36-481f6063dcde.png)

за допомогою команди - " docker pull panasyg/softwarenetictask " .
- наступною командою запускаємо контейнер - " docker run panasyg/softwarenetictask:latest " .
 ![image](https://user-images.githubusercontent.com/91308486/180341318-5bbe2b28-f46b-4aec-813d-092b85d1a349.png)
 
- далі переходимо за посиланням у браузері (або ж ThunderClient у VS code) - http://localhost:8000/healthcheck

Що ми бачимо ?
У відповідь на "/healthcheck" наш сервер повертає html-сторінку ( Ok ) 
![image](https://user-images.githubusercontent.com/91308486/180340688-3fe6af15-5bcc-4320-9370-583406505617.png)
![image](https://user-images.githubusercontent.com/91308486/180340494-32654035-9027-4065-b62c-d3feb51de477.png)

У всіх інших випадках - response(404)
![image](https://user-images.githubusercontent.com/91308486/180340956-015d4ac6-ff13-4ca5-bcb8-c3a02d92cf82.png)
![image](https://user-images.githubusercontent.com/91308486/180341063-035ca2a1-0d8d-48d4-9ca1-e88e47548d38.png)
![image](https://user-images.githubusercontent.com/91308486/180341095-9468a62d-06f4-426a-9111-6d037006c477.png)

