# Instagram Clone [FastAPI/React]

![React](https://i.postimg.cc/pLVGZtNh/2021-11-10-17-39-22.png)
![FastAPI](https://i.postimg.cc/rmdFRby7/2021-11-10-17-39-37.png)

## How to run and test it / Как запустить и протестировать приложение

1. Run the server-side FastAPI app in one terminal window / Запустить бэкэнд часть FastAPI в одном окне терминала:

    ```sh
    $ cd backend
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ uvicorn main:app --reload
    ```

    Navigate to / Перейдите по [http://localhost:8000](http://localhost:8000)

2. Run the client-side React app in a different terminal window / Запустить фронтэнд часть React во втором окне терминала:

    ```sh
    $ cd frontend
    $ npm start
    ```

    Navigate to / Перейдите по [http://localhost:3000](http://localhost:3000)
    
3. Sign up, select an image, add a caption and click Upload. / Зарегистрироваться, выбрать изображение, добавить надпись и нажать загрузить.

## Libraries used / Использованные библиотеки:

1. Backend
     ```sh
    fastapi
    uvicorn
    sqlalchemy
    passlib
    bcrypt
    python-multipart
    aiofiles
    python-jose
    ```
2. Frontend
    ```sh
    react.js
    material-ui/core
    ```
   
