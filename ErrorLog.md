Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-1075-realtime aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed Dec 25 05:07:58 PM UTC 2024

  System load:  2.38               Processes:               423
  Usage of /:   96.1% of 96.73GB   Users logged in:         0
  Memory usage: 7%                 IPv4 address for enp0s3: 10.0.0.35
  Swap usage:   0%

  => / is using 96.1% of 96.73GB

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is enabled.

0 updates can be applied immediately.


Last login: Wed Dec 25 16:44:05 2024 from 223.185.47.1
ubuntu@shamil:~$ cd PettyProjects/Challenger\ 2025/Challenger/
ubuntu@shamil:~/PettyProjects/Challenger 2025/Challenger$ docker-compose up --build -d -t 0 && docker-compose logs --tail 100 -f
[+] Building 1.3s (40/40) FINISHED                                                                                                  
 => [base-image internal] load build definition from base.Dockerfile                                                           0.0s
 => => transferring dockerfile: 517B                                                                                           0.0s
 => [worker internal] load build definition from Dockerfile                                                                    0.0s
 => => transferring dockerfile: 409B                                                                                           0.0s
 => [base-image internal] load metadata for docker.io/library/python:3.12-alpine                                               0.8s
 => [bot internal] load metadata for docker.io/library/yt-base-image:latest                                                    0.0s
 => [worker internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 249B                                                                                              0.0s
 => [bot 1/6] FROM docker.io/library/yt-base-image:latest                                                                      0.0s
 => [worker internal] load build context                                                                                       0.0s
 => => transferring context: 77.86kB                                                                                           0.0s
 => CACHED [worker 2/7] RUN apk add --no-cache ffmpeg                                                                          0.0s
 => CACHED [worker 3/7] COPY ./app_worker/requirements.txt ./                                                                  0.0s
 => CACHED [worker 4/7] RUN apk add --no-cache --virtual .build-deps         build-base     && MAKEFLAGS="-j$(nproc)" pip ins  0.0s
 => CACHED [worker 5/7] COPY ./app_worker ./start.py ./                                                                        0.0s
 => CACHED [worker 6/7] COPY yt_shared /app/yt_shared                                                                          0.0s
 => CACHED [worker 7/7] RUN pip install -e /app/yt_shared                                                                      0.0s
 => [worker] exporting to image                                                                                                0.0s
 => => exporting layers                                                                                                        0.0s
 => => writing image sha256:6ce5ae884a45f72a1583dd1a15e8833f0d7b851eee867ccc4fc154955983757c                                   0.0s
 => => naming to docker.io/library/yt-worker                                                                                   0.0s
 => [api internal] load build definition from Dockerfile                                                                       0.0s
 => => transferring dockerfile: 372B                                                                                           0.0s
 => [api internal] load .dockerignore                                                                                          0.0s
 => => transferring context: 249B                                                                                              0.0s
 => [api internal] load build context                                                                                          0.0s
 => => transferring context: 19.57kB                                                                                           0.0s
 => CACHED [api 2/6] COPY ./app_api/requirements.txt ./                                                                        0.0s
 => CACHED [api 3/6] RUN apk add --no-cache --virtual .build-deps         build-base     && MAKEFLAGS="-j$(nproc)" pip instal  0.0s
 => CACHED [api 4/6] COPY ./app_api ./start.py ./                                                                              0.0s
 => CACHED [api 5/6] COPY yt_shared /app/yt_shared                                                                             0.0s
 => CACHED [api 6/6] RUN pip install -e /app/yt_shared                                                                         0.0s
 => [api] exporting to image                                                                                                   0.0s
 => => exporting layers                                                                                                        0.0s
 => => writing image sha256:89e189ec1a5ec2228ad9b0e51d942c1d7fdfaf1eedf5be5ea33dda47708f355f                                   0.0s
 => => naming to docker.io/library/yt-api                                                                                      0.0s
 => [bot internal] load build definition from Dockerfile                                                                       0.0s
 => => transferring dockerfile: 372B                                                                                           0.0s
 => [base-image internal] load .dockerignore                                                                                   0.0s
 => => transferring context: 249B                                                                                              0.0s
 => [bot internal] load .dockerignore                                                                                          0.0s
 => => transferring context: 249B                                                                                              0.0s
 => [base-image 1/5] FROM docker.io/library/python:3.12-alpine@sha256:fd340d298d9d537a33c859f03bcc60e8e2542968e16f998bb0e232e  0.0s
 => [base-image internal] load build context                                                                                   0.0s
 => => transferring context: 84B                                                                                               0.0s
 => CACHED [base-image 2/5] RUN apk add --no-cache         tzdata         htop         bash         libstdc++                  0.0s
 => CACHED [base-image 3/5] WORKDIR /app                                                                                       0.0s
 => CACHED [base-image 4/5] COPY ./yt_shared/requirements_shared.txt ./                                                        0.0s
 => CACHED [base-image 5/5] RUN apk add --no-cache --virtual .build-deps         build-base     && apk add git     && pip ins  0.0s
 => [bot internal] load build context                                                                                          0.0s
 => => transferring context: 110.17kB                                                                                          0.0s
 => [base-image] exporting to image                                                                                            0.0s
 => => exporting layers                                                                                                        0.0s
 => => writing image sha256:d28e5db730bad3f66832850b1237c5952cd636247b9e56bc949222de8feefaa2                                   0.0s
 => => naming to docker.io/library/yt-base-image                                                                               0.0s
 => CACHED [bot 2/6] COPY ./app_bot/requirements.txt ./                                                                        0.0s
 => CACHED [bot 3/6] RUN apk add --no-cache --virtual .build-deps         build-base     && MAKEFLAGS="-j$(nproc)" pip instal  0.0s
 => CACHED [bot 4/6] COPY ./app_bot ./start.py ./                                                                              0.0s
 => CACHED [bot 5/6] COPY yt_shared /app/yt_shared                                                                             0.0s
 => CACHED [bot 6/6] RUN pip install -e /app/yt_shared                                                                         0.0s
 => [bot] exporting to image                                                                                                   0.0s
 => => exporting layers                                                                                                        0.0s
 => => writing image sha256:50c71d08a0e0709b3c9100a9d4f23813c90fdb92029ec4a17b130f53cb542c4a                                   0.0s
 => => naming to docker.io/library/yt-bot                                                                                      0.0s
[+] Running 6/0
 ✔ Container yt_rabbitmq  Running                                                                                              0.0s 
 ✔ Container yt_postgres  Running                                                                                              0.0s 
 ✔ Container yt_redis     Running                                                                                              0.0s 
 ✔ Container yt_worker    Running                                                                                              0.0s 
 ✔ Container yt_bot       Running                                                                                              0.0s 
 ✔ Container yt_api       Started                                                                                              0.0s 
yt_postgres  | 
yt_postgres  | 
yt_postgres  | PostgreSQL Database directory appears to contain a database; Skipping initialization
yt_postgres  | 
yt_postgres  | 
yt_postgres  | 2024-12-24 17:45:10.823 UTC [1] LOG:  starting PostgreSQL 14.8 (Debian 14.8-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
yt_postgres  | 2024-12-24 17:45:10.823 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
yt_postgres  | 2024-12-24 17:45:10.823 UTC [1] LOG:  listening on IPv6 address "::", port 5432
yt_postgres  | 2024-12-24 17:45:10.833 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
yt_postgres  | 2024-12-24 17:45:10.840 UTC [27] LOG:  database system was interrupted; last known up at 2024-12-24 17:43:59 UTC
yt_postgres  | 2024-12-24 17:45:10.860 UTC [27] LOG:  database system was not properly shut down; automatic recovery in progress
yt_postgres  | 2024-12-24 17:45:10.864 UTC [27] LOG:  redo starts at 0/A1CD080
yt_postgres  | 2024-12-24 17:45:10.864 UTC [27] LOG:  invalid record length at 0/A1CD168: wanted 24, got 0
yt_postgres  | 2024-12-24 17:45:10.864 UTC [27] LOG:  redo done at 0/A1CD130 system usage: CPU: user: 0.00 s, system: 0.00 s, elapsed: 0.00 s
yt_postgres  | 2024-12-24 17:45:10.895 UTC [1] LOG:  database system is ready to accept connections
yt_postgres  | 2024-12-24 17:58:27.055 UTC [1] LOG:  received fast shutdown request
yt_postgres  | 2024-12-24 17:58:27.063 UTC [1] LOG:  aborting any active transactions
yt_postgres  | 2024-12-24 17:58:27.064 UTC [67] FATAL:  terminating connection due to administrator command
yt_postgres  | 2024-12-24 17:58:27.070 UTC [62] FATAL:  terminating connection due to administrator command
yt_postgres  | 2024-12-24 17:58:27.103 UTC [1] LOG:  background worker "logical replication launcher" (PID 33) exited with exit code 1
yt_postgres  | 2024-12-24 17:58:27.143 UTC [28] LOG:  shutting down
yt_postgres  | 2024-12-24 17:58:27.194 UTC [1] LOG:  database system is shut down
yt_postgres  | 
yt_postgres  | 
yt_postgres  | PostgreSQL Database directory appears to contain a database; Skipping initialization
yt_postgres  | 
yt_postgres  | 
yt_postgres  | 2024-12-24 18:00:31.205 UTC [1] LOG:  starting PostgreSQL 14.8 (Debian 14.8-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
yt_postgres  | 2024-12-24 18:00:31.207 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
yt_postgres  | 2024-12-24 18:00:31.207 UTC [1] LOG:  listening on IPv6 address "::", port 5432
yt_postgres  | 2024-12-24 18:00:31.213 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
yt_postgres  | 2024-12-24 18:00:31.224 UTC [28] LOG:  database system was shut down at 2024-12-24 17:58:27 UTC
yt_postgres  | 2024-12-24 18:00:31.254 UTC [1] LOG:  database system is ready to accept connections
yt_postgres  | 2024-12-25 16:56:52.170 UTC [1] LOG:  received fast shutdown request
yt_postgres  | 2024-12-25 16:56:52.174 UTC [1] LOG:  aborting any active transactions
yt_postgres  | 2024-12-25 16:56:52.174 UTC [2740] FATAL:  terminating connection due to administrator command
yt_postgres  | 2024-12-25 16:56:52.175 UTC [40] FATAL:  terminating connection due to administrator command
yt_postgres  | 2024-12-25 16:56:52.192 UTC [1] LOG:  background worker "logical replication launcher" (PID 34) exited with exit code 1
yt_postgres  | 2024-12-25 16:56:52.200 UTC [29] LOG:  shutting down
yt_postgres  | 2024-12-25 16:56:52.229 UTC [1] LOG:  database system is shut down
yt_postgres  | 
yt_postgres  | 
yt_postgres  | PostgreSQL Database directory appears to contain a database; Skipping initialization
yt_postgres  | 
yt_postgres  | 
yt_postgres  | 2024-12-25 16:57:35.176 UTC [1] LOG:  starting PostgreSQL 14.8 (Debian 14.8-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
yt_postgres  | 2024-12-25 16:57:35.177 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
yt_postgres  | 2024-12-25 16:57:35.178 UTC [1] LOG:  listening on IPv6 address "::", port 5432
yt_postgres  | 2024-12-25 16:57:35.182 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
yt_postgres  | 2024-12-25 16:57:35.191 UTC [27] LOG:  database system was shut down at 2024-12-25 16:56:52 UTC
yt_postgres  | 2024-12-25 16:57:35.216 UTC [1] LOG:  database system is ready to accept connections
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [PostgreSQL] Waiting to be reachable on port 5432
yt_bot       | [RabbitMQ] Connection on port 5672 verified
yt_bot       | [PostgreSQL] Connection on port 5432 verified
yt_bot       | 2024-12-25 16:44:51,518 - [INFO] - [VideoBotClient:21] - Initializing bot client
yt_bot       | 2024-12-25 16:44:51,912 - [WARNING] - [asyncio:118] - Executing <Task pending name='Task-1' coro=<main() running at /app/main.py:14> wait_for=<Future pending cb=[Task.task_wakeup()] created at /usr/local/lib/python3.12/asyncio/streams.py:48> cb=[run_until_complete.<locals>.done_cb()] created at /usr/local/lib/python3.12/asyncio/runners.py:100> took 0.351 seconds
yt_bot       | 2024-12-25 16:44:56,389 - [INFO] - [BotLauncher:87] - Starting "Challenger"
yt_bot       | 2024-12-25 16:44:56,389 - [INFO] - [VideoBotClient:48] - Sending welcome message
yt_bot       | 2024-12-25 16:44:57,494 - [INFO] - [RabbitWorkerManager:29] - Starting ErrorDownloadResultWorker
yt_bot       | 2024-12-25 16:44:57,495 - [INFO] - [RabbitWorkerManager:29] - Starting SuccessDownloadResultWorker
yt_bot       | 2024-12-25 16:44:57,496 - [INFO] - [YtdlpNewVersionNotifyTask:40] - Checking for new STABLE yt-dlp version
yt_bot       | 2024-12-25 16:44:57,592 - [INFO] - [YtdlpVersionChecker:30] - Current yt-dlp version: 2024.12.23.232812
yt_bot       | 2024-12-25 16:44:58,066 - [INFO] - [YtdlpVersionChecker:25] - Latest yt-dlp version: 2024.12.23
yt_bot       | 2024-12-25 16:44:58,750 - [INFO] - [YtdlpNewVersionNotifyTask:47] - Next STABLE yt-dlp version check planned at 2024-12-26 16:44:58+00:00
yt_bot       | 2024-12-25 16:56:52,206 - [ERROR] - [aiormq.connection:565] - Unexpected connection close from remote "amqp://guest:******@yt_rabbitmq:5672/", Connection.Close(reply_code=320, reply_text="CONNECTION_FORCED - broker forced connection closure with reason 'shutdown'")
yt_bot       | NoneType: None
yt_bot       | 2024-12-25 16:56:52,213 - [INFO] - [aio_pika.robust_connection:83] - Connection to amqp://guest:******@yt_rabbitmq:5672/ closed. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:52,238 - [INFO] - [aio_pika.robust_connection:83] - Connection to amqp://guest:******@yt_rabbitmq:5672/ closed. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:52,238 - [WARNING] - [aio_pika.robust_connection:146] - Connection attempt to "amqp://guest:******@yt_rabbitmq:5672/" failed: [Errno 111] Connection refused. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:54,242 - [INFO] - [aio_pika.robust_connection:83] - Connection to amqp://guest:******@yt_rabbitmq:5672/ closed. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:54,242 - [WARNING] - [aio_pika.robust_connection:146] - Connection attempt to "amqp://guest:******@yt_rabbitmq:5672/" failed: [Errno 111] Connection refused. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:56,247 - [INFO] - [aio_pika.robust_connection:83] - Connection to amqp://guest:******@yt_rabbitmq:5672/ closed. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:56,247 - [WARNING] - [aio_pika.robust_connection:146] - Connection attempt to "amqp://guest:******@yt_rabbitmq:5672/" failed: [Errno 111] Connection refused. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:58,251 - [INFO] - [aio_pika.robust_connection:83] - Connection to amqp://guest:******@yt_rabbitmq:5672/ closed. Reconnecting after 2 seconds.
yt_bot       | 2024-12-25 16:56:58,252 - [WARNING] - [aio_pika.robust_connection:146] - Connection attempt to "amqp://guest:******@yt_rabbitmq:5672/" failed: [Errno 111] Connection refused. Reconnecting after 2 seconds.
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [PostgreSQL] Waiting to be reachable on port 5432
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [PostgreSQL] Waiting to be reachable on port 5432
yt_bot       | [PostgreSQL] Connection on port 5432 verified
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Waiting to be reachable on port 5672
yt_bot       | [RabbitMQ] Connection on port 5672 verified
yt_bot       | 2024-12-25 16:57:51,095 - [INFO] - [VideoBotClient:21] - Initializing bot client
yt_bot       | 2024-12-25 16:57:51,492 - [WARNING] - [asyncio:118] - Executing <Task pending name='Task-1' coro=<main() running at /app/main.py:14> wait_for=<Future pending cb=[Task.task_wakeup()] created at /usr/local/lib/python3.12/asyncio/streams.py:48> cb=[run_until_complete.<locals>.done_cb()] created at /usr/local/lib/python3.12/asyncio/runners.py:100> took 0.367 seconds
yt_bot       | 2024-12-25 16:57:52,719 - [INFO] - [BotLauncher:87] - Starting "Challenger"
yt_bot       | 2024-12-25 16:57:52,719 - [INFO] - [VideoBotClient:48] - Sending welcome message
yt_bot       | 2024-12-25 16:57:53,466 - [INFO] - [RabbitWorkerManager:29] - Starting ErrorDownloadResultWorker
yt_bot       | 2024-12-25 16:57:53,466 - [INFO] - [RabbitWorkerManager:29] - Starting SuccessDownloadResultWorker
yt_bot       | 2024-12-25 16:57:53,468 - [INFO] - [YtdlpNewVersionNotifyTask:40] - Checking for new STABLE yt-dlp version
yt_bot       | 2024-12-25 16:57:53,557 - [INFO] - [YtdlpVersionChecker:30] - Current yt-dlp version: 2024.12.23.232812
yt_bot       | 2024-12-25 16:57:54,421 - [INFO] - [YtdlpVersionChecker:25] - Latest yt-dlp version: 2024.12.23
yt_bot       | 2024-12-25 16:57:54,927 - [INFO] - [YtdlpNewVersionNotifyTask:47] - Next STABLE yt-dlp version check planned at 2024-12-26 16:57:54+00:00
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 742, in extract
yt_worker    |     ie_result = self._real_extract(url)
yt_worker    |                 ^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/youtube.py", line 4541, in _real_extract
yt_worker    |     self.raise_no_formats(reason, expected=True)
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 1276, in raise_no_formats
yt_worker    |     raise ExtractorError(msg, expected=expected, video_id=video_id)
yt_worker    | 
yt_worker    | 
yt_worker    | 2024-12-25 16:47:23,920 - [ERROR] - [MediaDownloader:72] - Error during media download. Check logs.. Meta: None
yt_worker    | 2024-12-25 16:47:23,920 - [ERROR] - [MediaDownloader:46] - Failed to download https://www.youtube.com/shorts/uduyHhE3mKY
yt_worker    | 2024-12-25 16:47:23,921 - [ERROR] - [MediaService:85] - Failed to download media. Context: id=None from_chat_id=1048186728 from_chat_type=<TelegramChatType.PRIVATE: 'private'> from_user_id=1048186728 message_id=8987 ack_message_id=8988 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 16, 47, 23, 199995, tzinfo=TzInfo(UTC))
yt_worker    | Traceback (most recent call last):
yt_worker    |   File "/app/worker/core/media_service.py", line 77, in _start_download
yt_worker    |     return await asyncio.get_running_loop().run_in_executor(
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/concurrent/futures/thread.py", line 59, in run
yt_worker    |     result = self.fn(*self.args, **self.kwargs)
yt_worker    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/media_service.py", line 79, in <lambda>
yt_worker    |     lambda: self._downloader.download(
yt_worker    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 44, in download
yt_worker    |     return self._download(host_conf=host_conf, media_payload=media_payload)
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 73, in _download
yt_rabbitmq  | 2024-12-25 16:57:44.367399+00:00 [info] <0.230.0> Running boot step tracking_metadata_store defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.367472+00:00 [info] <0.383.0> Setting up a table for connection tracking on this node: tracked_connection
yt_rabbitmq  | 2024-12-25 16:57:44.367513+00:00 [info] <0.383.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost
yt_rabbitmq  | 2024-12-25 16:57:44.367551+00:00 [info] <0.383.0> Setting up a table for per-user connection counting on this node: tracked_connection_per_user
yt_rabbitmq  | 2024-12-25 16:57:44.367619+00:00 [info] <0.383.0> Setting up a table for channel tracking on this node: tracked_channel
yt_rabbitmq  | 2024-12-25 16:57:44.367654+00:00 [info] <0.383.0> Setting up a table for channel tracking on this node: tracked_channel_per_user
yt_rabbitmq  | 2024-12-25 16:57:44.367763+00:00 [info] <0.230.0> Running boot step networking_metadata_store defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.367941+00:00 [info] <0.230.0> Running boot step database_sync defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368008+00:00 [info] <0.230.0> Running boot step feature_flags defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368138+00:00 [info] <0.230.0> Running boot step codec_correctness_check defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368165+00:00 [info] <0.230.0> Running boot step external_infrastructure defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368185+00:00 [info] <0.230.0> Running boot step rabbit_event defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368349+00:00 [info] <0.230.0> Running boot step rabbit_registry defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368488+00:00 [info] <0.230.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368589+00:00 [info] <0.230.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368653+00:00 [info] <0.230.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbityt_rabbitmq  | 2024-12-25 16:57:44.368728+00:00 [info] <0.230.0> Running boot step rabbit_exchange_type_direct defined by app rabbityt_rabbitmq  | 2024-12-25 16:57:44.368778+00:00 [info] <0.230.0> Running boot step rabbit_exchange_type_fanout defined by app rabbityt_rabbitmq  | 2024-12-25 16:57:44.368838+00:00 [info] <0.230.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368910+00:00 [info] <0.230.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.368977+00:00 [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369017+00:00 [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369058+00:00 [info] <0.230.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369084+00:00 [info] <0.230.0> Running boot step rabbit_priority_queue defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369105+00:00 [info] <0.230.0> Priority queues enabled, real BQ is rabbit_variable_queue
yt_rabbitmq  | 2024-12-25 16:57:44.369138+00:00 [info] <0.230.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369169+00:00 [info] <0.230.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369204+00:00 [info] <0.230.0> Running boot step rabbit_queue_location_random defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369232+00:00 [info] <0.230.0> Running boot step kernel_ready defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369258+00:00 [info] <0.230.0> Running boot step rabbit_sysmon_minder defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.369350+00:00 [info] <0.230.0> Running boot step rabbit_epmd_monitor defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.370199+00:00 [info] <0.392.0> epmd monitor knows us, inter-node communication (distribution) port: 25672
yt_rabbitmq  | 2024-12-25 16:57:44.370312+00:00 [info] <0.230.0> Running boot step guid_generator defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.373865+00:00 [info] <0.230.0> Running boot step rabbit_node_monitor defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.374082+00:00 [info] <0.396.0> Starting rabbit_node_monitor
yt_rabbitmq  | 2024-12-25 16:57:44.374205+00:00 [info] <0.230.0> Running boot step delegate_sup defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.374710+00:00 [info] <0.230.0> Running boot step rabbit_memory_monitor defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.375129+00:00 [info] <0.230.0> Running boot step rabbit_fifo_dlx_sup defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.375199+00:00 [info] <0.230.0> Running boot step core_initialized defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.375218+00:00 [info] <0.230.0> Running boot step upgrade_queues defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383102+00:00 [info] <0.230.0> Running boot step channel_tracking defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383165+00:00 [info] <0.230.0> Running boot step rabbit_channel_tracking_handler defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383244+00:00 [info] <0.230.0> Running boot step connection_tracking defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383323+00:00 [info] <0.230.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383366+00:00 [info] <0.230.0> Running boot step rabbit_definitions_hashing defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383465+00:00 [info] <0.230.0> Running boot step rabbit_exchange_parameters defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.383861+00:00 [info] <0.230.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.384188+00:00 [info] <0.230.0> Running boot step rabbit_policies defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.384456+00:00 [info] <0.230.0> Running boot step rabbit_policy defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.384515+00:00 [info] <0.230.0> Running boot step rabbit_queue_location_validator defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.384542+00:00 [info] <0.230.0> Running boot step rabbit_quorum_memory_manager defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.384567+00:00 [info] <0.230.0> Running boot step rabbit_stream_coordinator defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.385162+00:00 [info] <0.230.0> Running boot step rabbit_vhost_limit defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.385237+00:00 [info] <0.230.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
yt_rabbitmq  | 2024-12-25 16:57:44.385274+00:00 [info] <0.230.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
yt_rabbitmq  | 2024-12-25 16:57:44.385310+00:00 [info] <0.230.0> Management plugin: using rates mode 'basic'
yt_rabbitmq  | 2024-12-25 16:57:44.386968+00:00 [info] <0.230.0> Running boot step recovery defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.389724+00:00 [info] <0.430.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@cd408b10d0fd/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
yt_rabbitmq  | 2024-12-25 16:57:44.395916+00:00 [info] <0.430.0> Starting message stores for vhost '/'
yt_rabbitmq  | 2024-12-25 16:57:44.396613+00:00 [info] <0.435.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
yt_rabbitmq  | 2024-12-25 16:57:44.398739+00:00 [info] <0.430.0> Started message store of type transient for vhost '/'
yt_rabbitmq  | 2024-12-25 16:57:44.398921+00:00 [info] <0.439.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
yt_rabbitmq  | 2024-12-25 16:57:44.402186+00:00 [info] <0.430.0> Started message store of type persistent for vhost '/'
yt_rabbitmq  | 2024-12-25 16:57:44.408451+00:00 [info] <0.430.0> Recovering 3 queues of type rabbit_classic_queue took 17ms
yt_rabbitmq  | 2024-12-25 16:57:44.408733+00:00 [info] <0.430.0> Recovering 0 queues of type rabbit_quorum_queue took 0ms
yt_rabbitmq  | 2024-12-25 16:57:44.408784+00:00 [info] <0.430.0> Recovering 0 queues of type rabbit_stream_queue took 0ms
yt_rabbitmq  | 2024-12-25 16:57:44.411822+00:00 [info] <0.230.0> Running boot step empty_db_check defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412053+00:00 [info] <0.230.0> Will not seed default virtual host and user: have definitions to load...
yt_rabbitmq  | 2024-12-25 16:57:44.412084+00:00 [info] <0.230.0> Running boot step rabbit_observer_cli defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412152+00:00 [info] <0.230.0> Running boot step rabbit_looking_glass defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412181+00:00 [info] <0.230.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412312+00:00 [info] <0.230.0> Running boot step background_gc defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412429+00:00 [info] <0.230.0> Running boot step routing_ready defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412454+00:00 [info] <0.230.0> Running boot step pre_flight defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412469+00:00 [info] <0.230.0> Running boot step notify_cluster defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412489+00:00 [info] <0.230.0> Running boot step networking defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412556+00:00 [info] <0.230.0> Running boot step definition_import_worker_pool defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412583+00:00 [info] <0.351.0> Starting worker pool 'definition_import_pool' with 4 processes in it
yt_rabbitmq  | 2024-12-25 16:57:44.412812+00:00 [info] <0.230.0> Running boot step cluster_name defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412852+00:00 [info] <0.230.0> Running boot step direct_client defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412923+00:00 [info] <0.230.0> Running boot step rabbit_maintenance_mode_state defined by app rabbit
yt_rabbitmq  | 2024-12-25 16:57:44.412947+00:00 [info] <0.230.0> Creating table rabbit_node_maintenance_states for maintenance mode status
yt_rabbitmq  | 2024-12-25 16:57:44.413088+00:00 [info] <0.230.0> Running boot step rabbit_management_load_definitions defined by app rabbitmq_management
yt_rabbitmq  | 2024-12-25 16:57:44.413183+00:00 [info] <0.486.0> Resetting node maintenance status
yt_rabbitmq  | 2024-12-25 16:57:44.426687+00:00 [info] <0.545.0> Management plugin: HTTP (non-TLS) listener started on port 15672
yt_rabbitmq  | 2024-12-25 16:57:44.426863+00:00 [info] <0.573.0> Statistics database started.
yt_rabbitmq  | 2024-12-25 16:57:44.426938+00:00 [info] <0.572.0> Starting worker pool 'management_worker_pool' with 3 processes in it
yt_rabbitmq  | 2024-12-25 16:57:44.435915+00:00 [info] <0.587.0> Prometheus metrics: HTTP (non-TLS) listener started on port 15692
yt_rabbitmq  | 2024-12-25 16:57:44.436092+00:00 [info] <0.486.0> Ready to start client connection listeners
yt_rabbitmq  | 2024-12-25 16:57:44.437811+00:00 [info] <0.631.0> started TCP listener on [::]:5672
yt_rabbitmq  |  completed with 4 plugins.
yt_rabbitmq  | 2024-12-25 16:57:44.529027+00:00 [info] <0.486.0> Server startup complete; 4 plugins started.
yt_rabbitmq  | 2024-12-25 16:57:44.529027+00:00 [info] <0.486.0>  * rabbitmq_prometheus
yt_rabbitmq  | 2024-12-25 16:57:44.529027+00:00 [info] <0.486.0>  * rabbitmq_management
yt_rabbitmq  | 2024-12-25 16:57:44.529027+00:00 [info] <0.486.0>  * rabbitmq_web_dispatch
yt_rabbitmq  | 2024-12-25 16:57:44.529027+00:00 [info] <0.486.0>  * rabbitmq_management_agent
yt_rabbitmq  | 2024-12-25 16:57:49.068697+00:00 [info] <0.654.0> accepting AMQP connection <0.654.0> (172.18.0.6:55340 -> 172.18.0.5:5672)
yt_rabbitmq  | 2024-12-25 16:57:49.147838+00:00 [info] <0.654.0> connection <0.654.0> (172.18.0.6:55340 -> 172.18.0.5:5672): user 'guest' authenticated and granted access to vhost '/'
yt_rabbitmq  | 2024-12-25 16:57:51.102071+00:00 [info] <0.675.0> accepting AMQP connection <0.675.0> (172.18.0.3:39090 -> 172.18.0.5:5672)
yt_rabbitmq  | 2024-12-25 16:57:51.104880+00:00 [info] <0.675.0> connection <0.675.0> (172.18.0.3:39090 -> 172.18.0.5:5672): user 'guest' authenticated and granted access to vhost '/'
yt_worker    |     raise MediaDownloaderError(err_msg)
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_redis     | 1:C 24 Dec 2024 17:45:10.844 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
yt_redis     | 1:C 24 Dec 2024 17:45:10.844 # Redis version=7.0.12, bits=64, commit=00000000, modified=0, pid=1, just started
yt_redis     | 1:C 24 Dec 2024 17:45:10.844 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
yt_redis     | 1:M 24 Dec 2024 17:45:10.845 * monotonic clock: POSIX clock_gettime
yt_redis     | 1:M 24 Dec 2024 17:45:10.847 * Running mode=standalone, port=6379.
yt_redis     | 1:M 24 Dec 2024 17:45:10.847 # Server initialized
yt_redis     | 1:M 24 Dec 2024 17:45:10.850 * Ready to accept connections
yt_redis     | 1:signal-handler (1735063107) Received SIGTERM scheduling shutdown...
yt_redis     | 1:M 24 Dec 2024 17:58:27.200 # User requested shutdown...
yt_redis     | 1:M 24 Dec 2024 17:58:27.200 * Saving the final RDB snapshot before exiting.
yt_redis     | 1:M 24 Dec 2024 17:58:27.209 * DB saved on disk
yt_redis     | 1:M 24 Dec 2024 17:58:27.210 # Redis is now ready to exit, bye bye...
yt_redis     | 1:C 24 Dec 2024 18:00:30.639 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
yt_redis     | 1:C 24 Dec 2024 18:00:30.640 # Redis version=7.0.12, bits=64, commit=00000000, modified=0, pid=1, just started
yt_redis     | 1:C 24 Dec 2024 18:00:30.640 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
yt_redis     | 1:M 24 Dec 2024 18:00:30.641 * monotonic clock: POSIX clock_gettime
yt_redis     | 1:M 24 Dec 2024 18:00:30.661 * Running mode=standalone, port=6379.
yt_worker    | worker.core.exceptions.MediaDownloaderError: Error during media download. Check logs.
yt_worker    | 2024-12-25 16:47:23,929 - [INFO] - [RMQCallbacks:35] - Processing done with payload: id=None from_chat_id=1048186728 from_chat_type=<TelegramChatType.PRIVATE: 'private'> from_user_id=1048186728 message_id=8987 ack_message_id=8988 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 16, 47, 23, 199995, tzinfo=TzInfo(UTC))
yt_worker    | 2024-12-25 16:56:52,160 - [INFO] - [WorkerLauncher:78] - Shutting down WorkerLauncher
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [PostgreSQL] Waiting to be reachable on port 5432
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [PostgreSQL] Waiting to be reachable on port 5432
yt_worker    | [PostgreSQL] Connection on port 5432 verified
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Waiting to be reachable on port 5672
yt_worker    | [RabbitMQ] Connection on port 5672 verified
yt_worker    | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
yt_worker    | INFO  [alembic.runtime.migration] Will assume transactional DDL.
yt_worker    | 2024-12-25 16:57:49,036 - [INFO] - [WorkerLauncher:23] - Starting download worker instance
yt_worker    | 2024-12-25 16:57:49,038 - [INFO] - [WorkerLauncher:45] - Setting up RabbitMQ connection
yt_worker    | 2024-12-25 16:57:49,041 - [INFO] - [WorkerLauncher:54] - Saving current yt-dlp version (2024.12.23.232812) to the database
yt_worker    | 2024-12-25 16:57:49,055 - [INFO] - [WorkerLauncher:66] - Creating intermediate directories /tmp/download_tmpfs/downloading, /tmp/download_tmpfs/downloaded if not exist
yt_worker    | 2024-12-25 17:07:30,219 - [INFO] - [RMQCallbacks:25] - [x] Received message b'{"id":null,"from_chat_id":-1002397412457,"from_chat_type":"channel","from_user_id":null,"message_id":15,"ack_message_id":16,"url":"https://www.youtube.com/shorts/uduyHhE3mKY","original_url":"https://www.youtube.com/shorts/uduyHhE3mKY","source":"BOT","save_to_storage":false,"download_media_type":"VIDEO","custom_filename":null,"automatic_extension":false,"added_at":"2024-12-25T17:07:30.209210Z"}'
yt_worker    | 2024-12-25 17:07:30,294 - [INFO] - [DefaultHost:81] - Instantiating "DefaultHost" for url "https://www.youtube.com/shorts/uduyHhE3mKY"
yt_worker    | 2024-12-25 17:07:30,305 - [INFO] - [MediaDownloader:54] - Downloading https://www.youtube.com/shorts/uduyHhE3mKY, media_type VIDEO
yt_worker    | [debug] Override config: ['--output', '%(title).200B.%(ext)s', '--no-playlist', '--playlist-items', '1:1', '--concurrent-fragments', '5', '--ignore-errors', '--verbose', '--cookies', '/app/cookies/cookies.txt', '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '--write-thumbnail', '--convert-thumbnails', 'jpg', '--format-sort', 'res,vcodec:h265,h264']
yt_worker    | [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
yt_worker    | [debug] yt-dlp version nightly@2024.12.23.232812 from yt-dlp/yt-dlp-nightly-builds [65cf46cdd] (pip) API
yt_worker    | [debug] params: {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'format_sort': ['res', 'vcodec:h265', 'h264'], 'outtmpl': {'default': '/tmp/download_tmpfs/downloading/tmp_media_dir-1g9p8k8f/%(title).200B.%(ext)s'}, 'ignoreerrors': True, 'concurrent_fragment_downloads': 5, 'noplaylist': True, 'writethumbnail': True, 'verbose': True, 'cookiefile': '/app/cookies/cookies.txt', 'postprocessors': [{'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'}], 'playlist_items': '1:1', 'compat_opts': set(), 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}}
yt_worker    | [debug] Python 3.12.8 (CPython aarch64 64bit) - Linux-5.15.0-1075-realtime-aarch64-with (OpenSSL 3.3.2 3 Sep 2024)
yt_worker    | [debug] exe versions: ffmpeg 6.1.2 (setts), ffprobe 6.1.2
yt_worker    | [debug] Optional libraries: sqlite3-3.47.1
yt_worker    | [debug] Proxy map: {}
yt_worker    | [debug] Request Handlers: urllib
yt_worker    | [debug] Loaded 1837 extractors
yt_worker    | 2024-12-25 17:07:30,989 - [INFO] - [MediaDownloader:64] - Downloading "https://www.youtube.com/shorts/uduyHhE3mKY" to "/tmp/download_tmpfs/downloading/tmp_media_dir-1g9p8k8f"
yt_worker    | 2024-12-25 17:07:30,989 - [INFO] - [MediaDownloader:65] - Downloading with options: {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'format_sort': ['res', 'vcodec:h265', 'h264'], 'outtmpl': {'default': '/tmp/download_tmpfs/downloading/tmp_media_dir-1g9p8k8f/%(title).200B.%(ext)s', 'chapter': '%(title)s - %(section_number)03d %(section_title)s [%(id)s].%(ext)s'}, 'ignoreerrors': True, 'concurrent_fragment_downloads': 5, 'noplaylist': True, 'writethumbnail': True, 'verbose': True, 'cookiefile': '/app/cookies/cookies.txt', 'postprocessors': [{'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'}], 'playlist_items': '1:1', 'compat_opts': set(), 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'forceprint': {}, 'print_to_file': {}}
yt_worker    | [youtube] Extracting URL: https://www.youtube.com/shorts/uduyHhE3mKY
yt_worker    | [youtube] uduyHhE3mKY: Downloading webpage
yt_worker    | [debug] [youtube] Extracted SAPISID cookie
yt_worker    | [debug] [youtube] Copying __Secure-3PAPISID cookie to SAPISID cookie
yt_worker    | [youtube] uduyHhE3mKY: Downloading web creator player API JSON
yt_worker    | [youtube] uduyHhE3mKY: Downloading mweb player API JSON
yt_worker    | ERROR: [youtube] uduyHhE3mKY: Sign in to confirm you’re not a bot. Use --cookies-from-browser or --cookies for the authentication. See  https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp  for how to manually pass cookies. Also see  https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies  for tips on effectively exporting YouTube cookies
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 742, in extract
yt_worker    |     ie_result = self._real_extract(url)
yt_worker    |                 ^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/youtube.py", line 4541, in _real_extract
yt_worker    |     self.raise_no_formats(reason, expected=True)
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 1276, in raise_no_formats
yt_worker    |     raise ExtractorError(msg, expected=expected, video_id=video_id)
yt_worker    | 
yt_worker    | 
yt_worker    | 2024-12-25 17:07:31,871 - [ERROR] - [MediaDownloader:72] - Error during media download. Check logs.. Meta: None
yt_worker    | 2024-12-25 17:07:31,872 - [ERROR] - [MediaDownloader:46] - Failed to download https://www.youtube.com/shorts/uduyHhE3mKY
yt_worker    | 2024-12-25 17:07:31,873 - [ERROR] - [MediaService:85] - Failed to download media. Context: id=None from_chat_id=-1002397412457 from_chat_type=<TelegramChatType.CHANNEL: 'channel'> from_user_id=None message_id=15 ack_message_id=16 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 17, 7, 30, 209210, tzinfo=TzInfo(UTC))
yt_worker    | Traceback (most recent call last):
yt_worker    |   File "/app/worker/core/media_service.py", line 77, in _start_download
yt_worker    |     return await asyncio.get_running_loop().run_in_executor(
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/concurrent/futures/thread.py", line 59, in run
yt_worker    |     result = self.fn(*self.args, **self.kwargs)
yt_worker    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_redis     | 1:M 24 Dec 2024 18:00:30.663 # Server initialized
yt_redis     | 1:M 24 Dec 2024 18:00:30.671 * Loading RDB produced by version 7.0.12
yt_redis     | 1:M 24 Dec 2024 18:00:30.671 * RDB age 123 seconds
yt_redis     | 1:M 24 Dec 2024 18:00:30.671 * RDB memory usage when created 0.85 Mb
yt_redis     | 1:M 24 Dec 2024 18:00:30.671 * Done loading RDB, keys loaded: 0, keys expired: 0.
yt_redis     | 1:M 24 Dec 2024 18:00:30.671 * DB loaded from disk: 0.002 seconds
yt_redis     | 1:M 24 Dec 2024 18:00:30.672 * Ready to accept connections
yt_redis     | 1:signal-handler (1735145812) Received SIGTERM scheduling shutdown...
yt_redis     | 1:M 25 Dec 2024 16:56:52.224 # User requested shutdown...
yt_redis     | 1:M 25 Dec 2024 16:56:52.224 * Saving the final RDB snapshot before exiting.
yt_redis     | 1:M 25 Dec 2024 16:56:52.248 * DB saved on disk
yt_redis     | 1:M 25 Dec 2024 16:56:52.248 # Redis is now ready to exit, bye bye...
yt_redis     | 1:C 25 Dec 2024 16:57:34.450 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
yt_redis     | 1:C 25 Dec 2024 16:57:34.450 # Redis version=7.0.12, bits=64, commit=00000000, modified=0, pid=1, just started
yt_redis     | 1:C 25 Dec 2024 16:57:34.450 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
yt_redis     | 1:M 25 Dec 2024 16:57:34.452 * monotonic clock: POSIX clock_gettime
yt_redis     | 1:M 25 Dec 2024 16:57:34.461 * Running mode=standalone, port=6379.
yt_redis     | 1:M 25 Dec 2024 16:57:34.461 # Server initialized
yt_redis     | 1:M 25 Dec 2024 16:57:34.467 * Loading RDB produced by version 7.0.12
yt_redis     | 1:M 25 Dec 2024 16:57:34.467 * RDB age 42 seconds
yt_redis     | 1:M 25 Dec 2024 16:57:34.467 * RDB memory usage when created 0.85 Mb
yt_redis     | 1:M 25 Dec 2024 16:57:34.468 * Done loading RDB, keys loaded: 0, keys expired: 0.
yt_redis     | 1:M 25 Dec 2024 16:57:34.469 * DB loaded from disk: 0.003 seconds
yt_redis     | 1:M 25 Dec 2024 16:57:34.469 * Ready to accept connections
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_api       | [RabbitMQ] Waiting to be reachable on port 5672
yt_api       | [PostgreSQL] Waiting to be reachable on port 5432
yt_api       | [RabbitMQ] Connection on port 5672 verified
yt_api       | [PostgreSQL] Connection on port 5432 verified
yt_worker    |   File "/app/worker/core/media_service.py", line 79, in <lambda>
yt_worker    |     lambda: self._downloader.download(
yt_worker    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 44, in download
yt_worker    |     return self._download(host_conf=host_conf, media_payload=media_payload)
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 73, in _download
yt_worker    |     raise MediaDownloaderError(err_msg)
yt_worker    | worker.core.exceptions.MediaDownloaderError: Error during media download. Check logs.
yt_worker    | 2024-12-25 17:07:31,884 - [INFO] - [RMQCallbacks:35] - Processing done with payload: id=None from_chat_id=-1002397412457 from_chat_type=<TelegramChatType.CHANNEL: 'channel'> from_user_id=None message_id=15 ack_message_id=16 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 17, 7, 30, 209210, tzinfo=TzInfo(UTC))
yt_worker    | 2024-12-25 17:09:44,413 - [INFO] - [RMQCallbacks:25] - [x] Received message b'{"id":null,"from_chat_id":-1002397412457,"from_chat_type":"channel","from_user_id":null,"message_id":18,"ack_message_id":19,"url":"https://www.youtube.com/shorts/uduyHhE3mKY","original_url":"https://www.youtube.com/shorts/uduyHhE3mKY","source":"BOT","save_to_storage":false,"download_media_type":"VIDEO","custom_filename":null,"automatic_extension":false,"added_at":"2024-12-25T17:09:44.410511Z"}'
yt_worker    | 2024-12-25 17:09:44,419 - [INFO] - [DefaultHost:81] - Instantiating "DefaultHost" for url "https://www.youtube.com/shorts/uduyHhE3mKY"
yt_worker    | 2024-12-25 17:09:44,424 - [INFO] - [MediaDownloader:54] - Downloading https://www.youtube.com/shorts/uduyHhE3mKY, media_type VIDEO
yt_worker    | [debug] Override config: ['--output', '%(title).200B.%(ext)s', '--no-playlist', '--playlist-items', '1:1', '--concurrent-fragments', '5', '--ignore-errors', '--verbose', '--cookies', '/app/cookies/cookies.txt', '--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '--write-thumbnail', '--convert-thumbnails', 'jpg', '--format-sort', 'res,vcodec:h265,h264']
yt_worker    | [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
yt_worker    | [debug] yt-dlp version nightly@2024.12.23.232812 from yt-dlp/yt-dlp-nightly-builds [65cf46cdd] (pip) API
yt_worker    | [debug] params: {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'format_sort': ['res', 'vcodec:h265', 'h264'], 'outtmpl': {'default': '/tmp/download_tmpfs/downloading/tmp_media_dir-0hzkiitu/%(title).200B.%(ext)s'}, 'ignoreerrors': True, 'concurrent_fragment_downloads': 5, 'noplaylist': True, 'writethumbnail': True, 'verbose': True, 'cookiefile': '/app/cookies/cookies.txt', 'postprocessors': [{'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'}], 'playlist_items': '1:1', 'compat_opts': set(), 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}}
yt_worker    | [debug] Python 3.12.8 (CPython aarch64 64bit) - Linux-5.15.0-1075-realtime-aarch64-with (OpenSSL 3.3.2 3 Sep 2024)
yt_worker    | [debug] exe versions: ffmpeg 6.1.2 (setts), ffprobe 6.1.2
yt_worker    | [debug] Optional libraries: sqlite3-3.47.1
yt_worker    | [debug] Proxy map: {}
yt_worker    | [debug] Request Handlers: urllib
yt_worker    | [debug] Loaded 1837 extractors
yt_worker    | 2024-12-25 17:09:44,513 - [INFO] - [MediaDownloader:64] - Downloading "https://www.youtube.com/shorts/uduyHhE3mKY" to "/tmp/download_tmpfs/downloading/tmp_media_dir-0hzkiitu"
yt_worker    | 2024-12-25 17:09:44,513 - [INFO] - [MediaDownloader:65] - Downloading with options: {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'format_sort': ['res', 'vcodec:h265', 'h264'], 'outtmpl': {'default': '/tmp/download_tmpfs/downloading/tmp_media_dir-0hzkiitu/%(title).200B.%(ext)s', 'chapter': '%(title)s - %(section_number)03d %(section_title)s [%(id)s].%(ext)s'}, 'ignoreerrors': True, 'concurrent_fragment_downloads': 5, 'noplaylist': True, 'writethumbnail': True, 'verbose': True, 'cookiefile': '/app/cookies/cookies.txt', 'postprocessors': [{'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'}], 'playlist_items': '1:1', 'compat_opts': set(), 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'forceprint': {}, 'print_to_file': {}}
yt_worker    | [youtube] Extracting URL: https://www.youtube.com/shorts/uduyHhE3mKY
yt_worker    | [youtube] uduyHhE3mKY: Downloading webpage
yt_worker    | [debug] [youtube] Extracted SAPISID cookie
yt_worker    | [debug] [youtube] Copying __Secure-3PAPISID cookie to SAPISID cookie
yt_worker    | [youtube] uduyHhE3mKY: Downloading web creator player API JSON
yt_worker    | [youtube] uduyHhE3mKY: Downloading mweb player API JSON
yt_worker    | ERROR: [youtube] uduyHhE3mKY: Sign in to confirm you’re not a bot. Use --cookies-from-browser or --cookies for the authentication. See  https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp  for how to manually pass cookies. Also see  https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies  for tips on effectively exporting YouTube cookies
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 742, in extract
yt_worker    |     ie_result = self._real_extract(url)
yt_worker    |                 ^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/youtube.py", line 4541, in _real_extract
yt_worker    |     self.raise_no_formats(reason, expected=True)
yt_worker    |   File "/usr/local/lib/python3.12/site-packages/yt_dlp/extractor/common.py", line 1276, in raise_no_formats
yt_worker    |     raise ExtractorError(msg, expected=expected, video_id=video_id)
yt_worker    | 
yt_worker    | 
yt_worker    | 2024-12-25 17:09:45,251 - [ERROR] - [MediaDownloader:72] - Error during media download. Check logs.. Meta: None
yt_worker    | 2024-12-25 17:09:45,252 - [ERROR] - [MediaDownloader:46] - Failed to download https://www.youtube.com/shorts/uduyHhE3mKY
yt_worker    | 2024-12-25 17:09:45,252 - [ERROR] - [MediaService:85] - Failed to download media. Context: id=None from_chat_id=-1002397412457 from_chat_type=<TelegramChatType.CHANNEL: 'channel'> from_user_id=None message_id=18 ack_message_id=19 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 17, 9, 44, 410511, tzinfo=TzInfo(UTC))
yt_worker    | Traceback (most recent call last):
yt_worker    |   File "/app/worker/core/media_service.py", line 77, in _start_download
yt_worker    |     return await asyncio.get_running_loop().run_in_executor(
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/usr/local/lib/python3.12/concurrent/futures/thread.py", line 59, in run
yt_worker    |     result = self.fn(*self.args, **self.kwargs)
yt_worker    |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/media_service.py", line 79, in <lambda>
yt_worker    |     lambda: self._downloader.download(
yt_worker    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 44, in download
yt_worker    |     return self._download(host_conf=host_conf, media_payload=media_payload)
yt_worker    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
yt_worker    |   File "/app/worker/core/downloader.py", line 73, in _download
yt_worker    |     raise MediaDownloaderError(err_msg)
yt_worker    | worker.core.exceptions.MediaDownloaderError: Error during media download. Check logs.
yt_worker    | 2024-12-25 17:09:45,260 - [INFO] - [RMQCallbacks:35] - Processing done with payload: id=None from_chat_id=-1002397412457 from_chat_type=<TelegramChatType.CHANNEL: 'channel'> from_user_id=None message_id=18 ack_message_id=19 url='https://www.youtube.com/shorts/uduyHhE3mKY' original_url='https://www.youtube.com/shorts/uduyHhE3mKY' source=<TaskSource.BOT: 'BOT'> save_to_storage=False download_media_type=<DownMediaType.VIDEO: 'VIDEO'> custom_filename=None automatic_extension=False added_at=datetime.datetime(2024, 12, 25, 17, 9, 44, 410511, tzinfo=TzInfo(UTC))