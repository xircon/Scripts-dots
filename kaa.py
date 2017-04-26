import time, socket, errno
import KAA

@kaa.timed(1)
def timer():
    "This function is invoked every second from the main loop."
    print('timer fired at', time.time())


@kaa.threaded()
def thread(count):
    "This function runs in a thread.  Notice it blocks."
    for i in range(count):
        print('thread woke up at', time.time())
        time.sleep(1)


@kaa.coroutine()
def coroutine():
    "By yielding, this function can have multiple reentry points."
    # We can spawn a new instance of thread().  The coroutine will reenter
    # after thread() finishes, but the main loop is not blocked; the timer
    # we started keeps firing all the while.
    print('coroutine starting')
    yield thread(3)

    # Sub-process IO doesn't block.
    stdout, stderr = yield kaa.Process('lsusb').communicate()

    # And of course sockets don't block. Notice that asynchronously
    # generated exceptions can be handled as if you were writing typical
    # blocking code.
    sock = kaa.Socket()
    try:
        yield sock.connect('www.freevo.org:80')
    except socket.error as e:
        print('Connection failed:', e.strerror)
    else:
        sock.write('GET / HTTP/1.0\n\n')
        webpage = yield sock.read()
        print(webpage)

    # We can yield back to the main loop at any time.
    yield kaa.NotFinished

    # Or we can be reentered after some (non-blocking) period of time.
    yield kaa.delay(2)

    # Ok, let's shut everything down.  Main loop stops and coroutine exits.
    kaa.main.stop()
    print('coroutine done')

# Start a new thread that runs thread() inside it.
thread(10)
# Start the timed function
timer()
# Invoke the coroutine.  It will immediately execute everything before the
# first yield and then return, having scheduled itself for reentry.
coroutine()
# Start the main loop.  This blocks until explicitly stopped, or if
# KeyboardInterrupt or SystemExit is raised, or if there is an uncaught
# exception.
kaa.main.run()
