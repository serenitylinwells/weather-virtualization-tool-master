if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', port=8081, reload=True)
