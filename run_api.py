import uvicorn
hostipapi = "0.0.0.0"
portipapi = 8000
DEBUG = True
#ruta al key y certificado free generado con openssl
#key = BASE_DIR / 'ssl/cert.key'
#crt = BASE_DIR / 'ssl/cert.pem'

if __name__ == '__main__':
    uvicorn.run("api:app",
            host=hostipapi,
            port=portipapi,
            #ssl_keyfile=key,
            #ssl_certfile=crt,
            #log_level='error',
            #loop='asyncio',
            #workers=4,
            #limit_concurrency=10,
            #limit_max_requests=30,
            lifespan='on',
            timeout_keep_alive=5,
            reload=DEBUG
            )
