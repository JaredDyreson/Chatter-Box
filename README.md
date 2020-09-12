# Chatter-Box

A chat  service written in Python

## Usage

Run the following command in one terminal window:

```bash
./start_chatter_server.py
```

And then open another terminal window in the same directory and run:

```bash
./chatter.py
```

The result should be:

```
Example text
```

This is a proof of concept of how to start a server that will take input and dish it out to multiple connections to the server.


## TODO

- [ ] Send data from client to sever (it is vice versa right now)
- [ ] Make it more user friendly
- [ ] Encapsulated having to run the server manually and have python handle that (multithreading or multiprocessing, not too sure which)
- [ ] Better documentation
- [ ] Unit tests
