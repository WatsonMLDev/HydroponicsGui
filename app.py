import os
import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()
    import main
    mainInstance = main.Main()
    mainInstance.app.run(host="0.0.0.0", debug=False)