## What is this?

When you need to quickly copy a file from a computer to another, what would you do?

- Use a USB stick and copy-pasting twice? With that slow thing? No no no!
- Google Drive? Ngl every Google app is laggy AF. Every click costs a few seconds.
- Use sites like Google Drive? Or maybe just send files through messaging apps? Nah there are too many limit, and they have that "antivirus" thing.
- Torrent? Who the hell create a torrent for one-time use lol.

And that's why I created this abomination:

![2022-09-05_13-28](https://user-images.githubusercontent.com/58514512/188375626-b84737d5-f06c-4879-820b-d30e22d221a0.png)

## How to use

Create this directory if not exists:

```
./portal/static/f/
```

Let's call that directory as `ROOT`.

In `ROOT`, create some more directories as channels. Put files to those channels to get them shared. Sounds like Discord, heh?

To run server, simply follow `manage.py`'s instruction. For example: 

```
python manage.py runserver 0.0.0.0:4002
```

