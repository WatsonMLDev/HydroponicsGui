import multiprocessing

if __name__ == "__main__":

    multiprocessing.freeze_support()
    import main

    main.app.run(host="0.0.0.0", debug=True)