# 🧩 Add your ressources to [Malfrat's OSINT Map](https://map.malfrats.industries)
- **Fork [the repository](https://github.com/Malfrats/OSINT-Map)**
- You should now be in your forked repository.
  - _If not, go to `https://github.com/<YOUR USERNAME>/OSINT-Map`, and then you're in._
- **Go in `/database.json`**
- **Edit the file** then **save it**.
  - _If you want your project to be merged, follow the rules and tutorial following this part._
- Submit a **pull request**, and wait for your project being merged to Malfrat's OSINT MAP !
## 📏 Rules:
Every pull request will be checked, and if it does not respect the following lines, will be declined.
1. The tool **must be in a branch**, and **respect the specific Syntax** (specified at the next block).
2. If the tool has **no link with OSINT**, the pull request **will (_obviously_) be delined**.
    - _We will be rigorous in our choices concerning the contributions to keep the osint map coherent and interesting to the greatest number without degrading its quality, thank you for respecting this._
3. Please **put the ressources that are useful only for one region in its corresponding location name** in `Specific Regions`.
    - _If the region / country isn't made, you can create it and add its flag after a space at the end (if it doesn't have a flag, a symbol of this region)._
## 🖌 Syntax
1. Ressources names:
    - For the legend, precise **one** or **many emoji(s) from [this legend](https://github.com/Malfrats/OSINT-Map#-legend)**. _If there's many emojis, do not add space between emojis._
    - Add a space.
    - Add the name of your ressource. It can contain spaces.
2. Branch names:
    - You can put spaces in it, but **no emojis at the start** of the string.
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
