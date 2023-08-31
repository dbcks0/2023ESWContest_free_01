user@user:~ $ cd webcam
user@user:~/webcam $ ls
templates  webcam.py
user@user:~/webcam $ python webcam.py
 * Serving Flask app "webcam" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://192.168.1.107:8080/ (Press CTRL+C to quit)
192.168.1.100 - - [27/Aug/2023 08:29:52] "GET / HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:29:54] "GET /video_feed HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:30:12] "GET /favicon.ico HTTP/1.1" 404 -
192.168.1.100 - - [27/Aug/2023 08:36:07] "GET / HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:36:07] "GET /video_feed HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:36:27] "GET /favicon.ico HTTP/1.1" 404 -
192.168.1.100 - - [27/Aug/2023 08:53:17] "GET / HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:53:17] "GET /video_feed HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 08:53:37] "GET /favicon.ico HTTP/1.1" 404 -
192.168.1.100 - - [27/Aug/2023 09:09:04] "GET / HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 09:09:04] "GET /video_feed HTTP/1.1" 200 -
192.168.1.100 - - [27/Aug/2023 09:09:24] "GET /favicon.ico HTTP/1.1" 404 -
