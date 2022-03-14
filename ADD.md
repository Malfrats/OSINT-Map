# 🧩 Add your ressources to [Malfrat's OSINT Map](https://map.malfrats.industries)
- **Fork [the repository](https://github.com/Malfrats/OSINT-Map)**
- You should now be in your forked repository.
  - _If not, go to `https://github.com/<YOUR USERNAME>/OSINT-Map`, and then you're in._
- **Go in `/database.json`**
- **Edit the file** then **save it**.
  - _If you want your project to be merged, follow the rules and the tutorial following this part._
- Submit a **pull request**, and wait for your project being merged to Malfrat's OSINT MAP !
## 📏 Rules:
1. The tool **must be in a category**; precise the category with **an emoji from [this legend](https://github.com/Malfrats/OSINT-Map#-legend)** before a space separating it from the name of the tool.
   - Syntax: `<EMOJI> <NAME>`. Any space forgot between the legend emoji and the name will automatically decline the pull request.
      - _You can also combine two emojis, e.g.: if tool is online and has in-app purchases. The in-app purchases logo must be placed first._
   - Any non-existent or unspecified category will automatically decline the pull request.
2. If the tool has **no link with OSINT**, the pull request **will (_obviously_) be delined**.
## 🛠 Tutorial:
If you don't understand how work the json file, the following lines are for you !
### 📂 To add a new branch:
Let's admit I want to open in the `Usernames` branch a new one called `Alpha`, containing itself an empty branch `Beta`.
```python
# Before
{
    "OSINT Map": {
        "Usernames": {
            "📦 maigret": "https://github.com/soxoj/maigret"
        }
    }
}

# After
{
    "OSINT Map": {
        "Usernames": {
            "📦 maigret": "https://github.com/soxoj/maigret",
            "Alpha": {
                "Beta": {}
            }
        }
    }
}
```
### ♟ To add a new tool
Now, let's admit I want to add a tool to my brand new branch `Beta`:
```python
# Before
{
    "OSINT Map": {
        "Usernames": {
            "📦 maigret": "https://github.com/soxoj/maigret",
            "Alpha": {
                "Beta": {}
            }
        }
    }
}

# After
{
    "OSINT Map": {
        "Usernames": {
            "📦 maigret": "https://github.com/soxoj/maigret",
            "Alpha": {
                "Beta": {
                    "<CATEGORY EMOJI (check the rules)> <CATEGORY NAME>": "url://to.my.awesome/tool"
                }
            }
        }
    }
}
```
## 😉 See you soon in pull requests !
