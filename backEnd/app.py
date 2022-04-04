import multiprocessing
import main
import math

if __name__ == "__main__":

    multiprocessing.freeze_support()

    main.app.run(host="0.0.0.0", debug=True)