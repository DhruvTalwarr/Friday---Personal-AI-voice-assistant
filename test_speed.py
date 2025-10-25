import speedtest

def getSpeed():
    wifi = speedtest.Speedtest()
    wifi.get_servers([])  # fetch available servers
    wifi.get_best_server()
    download_speed = wifi.download() / 1_000_000  # Mbps
    upload_speed = wifi.upload() / 1_000_000      # Mbps
    return download_speed, upload_speed
