Title: getting indefinite input feed in hackerrank
Date: 2016-10-25 16:04
Category: code
Tags: python
Status: published

If you have been using [HackerRank][1] and encountered problems that accepts an indefinite amount of input from `STDIN` like this:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

and wodered how to get all that in a single list for later processing, here's a code snippet:

```python

""" your code goes here """

def main():
    data = []

    while True:
        try:
            line = input()
        except EOFError:
            break
        data.append(line)

    """ your code goes here """
    print(data)


if __name__ == '__main__':
    main()
```

From my observation, it seems the input is coming from a file and its being streamed to `STDIN` one line at a time.

[1]: http://www.hackerrank.com