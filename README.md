Для того аби підняти наш сервер:
- стягуємо образ з мого DockerHub( https://hub.docker.com/r/panasyg/softwarenetictask ) 
![image](https://user-images.githubusercontent.com/91308486/180342056-651837b1-4bad-4911-b79c-2e925c1aceeb.png)
за допомогою команди - " docker pull panasyg/softwarenetictask " .

- наступною командою запускаємо контейнер і спрямовуємо 8000 порт нашого контейнера на 8000 порт комп'ютера - 
" docker run -p 8000:8000 panasyg/softwarenetictask:latest " .
![image](https://user-images.githubusercontent.com/91308486/180342907-515ddacf-a176-457b-b727-e8836e894748.png)

- далі переходимо за посиланням у браузері (або ж ThunderClient у VS code) - http://localhost:8000/healthcheck

Що ми бачимо ?
У відповідь на "/healthcheck" наш сервер повертає html-сторінку ( Ok ) 
![image](https://user-images.githubusercontent.com/91308486/180343505-b78f8ec4-21a5-4a74-88b0-155305b45878.png)
![image](https://user-images.githubusercontent.com/91308486/180343544-5a568532-cf3b-4c8a-a8af-e148ea9579f7.png)

У всіх інших випадках - response(404)
![image](https://user-images.githubusercontent.com/91308486/180343614-8c11fdd9-94c2-4cef-9998-eb93a766b4f4.png)
![image](https://user-images.githubusercontent.com/91308486/180343660-124f4241-118a-475c-a55b-c0a15f15cf5e.png)
![image](https://user-images.githubusercontent.com/91308486/180343715-6d351816-4076-4eae-ae18-e4d8addb1234.png)

