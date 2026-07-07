import speedtest

def run_speed_test():
    try:
        st = speedtest.Speedtest()

        st.get_best_server()

        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        ping = round(st.results.ping, 2)

        return {
            "download": download,
            "upload": upload,
            "ping": ping
        }

    except Exception as e:
        return {
            "download": "Error",
            "upload": "Error",
            "ping": str(e)
        }