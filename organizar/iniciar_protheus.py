import os

def start_service(svc):
    os.system(f'net start {svc}')


start_service('licenseVirtual')
