# 🧩 Add your resources to [Malfrat's OSINT Map](https://map.malfrats.industries)
- **Fork [the repository](https://github.com/Malfrats/OSINT-Map)**
- You should now be in your forked repository.
  - _If not, go to `https://github.com/<YOUR USERNAME>/OSINT-Map`, and then you're in._
- **Go in `/database.json`**
- **Edit the file** then **save it**.
  - _If you want your project to be merged, follow the rules and tutorial following this part._
- Submit a **pull request**, and wait for your project being merged to Malfrat's OSINT MAP !
## 📏 Rules:
Every pull request will be reviewed, and if it does not meet the following guidelines, will be declined.
1. The tool **must be in a branch**, and **respect the specific syntax** (specified at the next section).
2. If the tool is **not related to OSINT**, the pull request **will (_obviously_) be delined**.
    - _We will be rigorous in our choices regarding the contributions to keep the osint map consistent and attractive to the greatest number without degrading its quality, thank you for respecting this._
3. Please **put the resources useful for a single region in its corresponding location name** in `Specific Regions`.
    - _If the region / country doesn't exist, you can create it and add its flag after a space at the end (if it doesn't have a flag, a symbol of this region)._
## 🖌 Syntax
1. Resources names:
    - For the legend, specify **one** or **many emoji(s) from [this legend](https://github.com/Malfrats/OSINT-Map#-legend)**. _If there's many emojis, do not add space between them._
    - Add a space.
    - Add the name of your resource. It can contain spaces.
2. Branch names:
    - You can put spaces in it, but **no emoji at the start** of the string.
## 🛠 Tutorial:
If you don't understand how the JSON file works, the following lines are for you !
### 📂 To add a new branch:
Let's say I want to open in the `Usernames` branch a new one called `Alpha`, containing itself an empty branch `Beta`.
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
Now, let's say I want to add a tool to my brand new branch `Beta`:
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
