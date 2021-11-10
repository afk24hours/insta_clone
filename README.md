# Instagram Clone [FastAPI/React]

## How to run and test it / Как запустить и протестировать приложение

1. Run the server-side FastAPI app in one terminal window / Запустить бэкэнд часть FastAPI в одном окне терминала:

    ```sh
    $ cd backend
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python uvicorn main:app --reload
    ```

    Navigate to / Перейдите по [http://localhost:8000](http://localhost:8000)

2. Run the client-side React app in a different terminal window / Запустить фронтэнд часть React во втором окне терминала:

    ```sh
    $ cd frontend
    $ npm install
    $ npm run start
    ```

    Navigate to / Перейдите по [http://localhost:3000](http://localhost:3000)
    
3. Sign up, select an image, add a caption and click Upload. / Зарегистрироваться, выбрать изображение, добавить надпись и нажать загрузить.
