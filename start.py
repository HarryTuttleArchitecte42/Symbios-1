import sys
sys.path.insert(0, '/app/deps')
import uvicorn

if __name__ == '__main__':
    uvicorn.run('synergyai-core.main:app', host='0.0.0.0', port=8080)
