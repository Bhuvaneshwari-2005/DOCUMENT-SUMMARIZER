import os, socket
from dotenv import load_dotenv
from zeroconf import ServiceInfo, Zeroconf

# Load environment variables from .env if it exists
load_dotenv()

from app import app, get_ip

if __name__ == "__main__":
    import time
    
    port = int(os.environ.get("PORT", 8080))
    ip = get_ip()
    
    desc = {'path': '/'}
    info = ServiceInfo(
        "_http._tcp.local.",
        "DOCUMENT-SUMMARIZER._http._tcp.local.",
        addresses=[socket.inet_aton(ip)],
        port=port,
        properties=desc,
        server="DOCUMENT-SUMMARIZER.local.",
    )
    
    zeroconf = Zeroconf()
    print(f"Broadcasting as DOCUMENT-SUMMARIZER.local on {ip}")
    print(f"URL: http://DOCUMENT-SUMMARIZER.local:{port}")
    print(f"Fallback: http://{ip}:{port}")
    
    registered = False
    for attempt in range(3):
        try:
            zeroconf.register_service(info)
            registered = True
            print("[OK] mDNS service registered successfully")
            break
        except Exception as e:
            print(f"[Attempt {attempt + 1}] mDNS registration failed: {str(e)[:50]}")
            if attempt < 2:
                time.sleep(1)
    
    if not registered:
        print("[WARNING] Could not register mDNS. App will run on IP only.")
    
    try:
        print(f"\nStarting application on port {port}...")
        app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
    finally:
        print("\nStopping application...")
        try:
            zeroconf.unregister_service(info)
            print("[OK] mDNS service unregistered")
        except Exception:
            pass
        zeroconf.close()
