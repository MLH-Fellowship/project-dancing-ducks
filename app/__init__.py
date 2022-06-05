import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

# dictionary of all information about fellows. Will be passed in a render_template call and used in a jinja template.
# "name": {
#         "first": "",
#         "last": "",
#         "about": "",
#         "image": "",
#         "socials": [
#             {
#                 "name": "",
#                 "link": ""
#             }
#         ],
#         "education": [
#             {
#                 "institution": "",
#                 "grad_date": "",
#                 "courses": "",
#             }
#         ],
#         "experience": [
#             {
#                 "position": "",
#                 "company": "",
#                 "dates": "",
#                 "desc": ""
#             }
#         ],
#         "resume": "",
#         "hobbies": [
#             {
#                 "name": "",
#                 "image": "",
#                 "desc": ""
#             }
            
#         ]
#     }
fellows = {
    "lucy": {
        "first": "Lucy",
        "last": "Wang",
        "about": "Hello! I am Lucy Wang. I'm majoring in Computer Science and minoring in Japanese at Villanova University.",
        "image": "",
        "socials": [
            {
                "name": "LinkedIn",
                "link": "https://www.linkedin.com/in/lucy-wang-a73267191/"
            }
        ],
        "education": [
            {
                "institution": "Villanova University",
                "grad_date": "May 2023",
                "courses": "Computer Science"
            }
        ],
        "experience": [
            {
                "position": "IT Assistant",
                "company": "Sepax Technologies, Inc.",
                "dates": "June 2020 - July 2020, May 2022 - August 2022",
                "desc": "I helped out with IT tasks. Troubleshooted problems with office machines (printers and computers) and issues with the local network. Used MySQL, HTML/CSS, Javascript, and PHP for web development of the intranet and external website. Utilized Python to log issues with servers hosting the db, website, intranet, and camera systems.",
            }
        ],
        "resume": "",
        "hobbies": [
            {
                "name": "Art",
                "image": "",
                "desc": "I love to draw! I mainly do sketches of characters in an anime style on my iPad. I love drawing for other people, especially if they have cool character designs!"
            },
            {
                "name": "Gaming",
                "image": "",
                "desc": "I'm a casual gamer. I only own a Macbook so I can't play a lot of games, so I just dabble in some mobile games! I mainly play Genshin Impact, but I also play Arknights. As for computer games, I'm currently playing Celeste! I've also casually played Minecraft, Terraria, and Portal.",
            },
            {
                "name": "Anime/Manga",
                "image": "anime.jpg",
                "desc": "As one might have guessed from my artistic hobby, I like watching anime and reading manga. My favorite manga is Chrono Crusade!"
            }
        ],
        "locations": [
            {
                "location": "China",
                "coordinates": [31.224361, 121.469170],
                "desc": "I visited my relatives in China when I was very young. I went to Shanghai, Xiangtan in Hunan province, and the countryside in Henan province. I don't remember much, but if you're visiting the countryside, definitely be prepared for the mosquitoes!"
            },
            {
                "location": "Taiwan",
                "coordinates": [22.999727, 120.227028],
                "desc": "I taught English to elementary and middle school students in various schools in Tainan, Taiwan for two weeks. I know Mandarin Chinese, but it was hard even when I had a teaching partner! At one school, we did not have enough people on our team and I had to teach solo! Still, it was a very exciting experience. Taiwan is a great place to visit!"
            },
            {
                "location": "Alaska",
                "coordinates": [63.129887, -151.197418],
                "desc": "I traveled to Alaska with family! The highlight of our trip was visiting Denali National Park, where we got to see Mt. Denali, moose, caribou, bears, and even a few wolves (in the distance). Alaska is full of preserved nature, which is evidenced by the fact bugs still get smashed against car windshields there!"
            },
            {
                "location": "Las Vegas, NV",
                "coordinates": [36.114647, -115.172813],
                "desc": "I visited Las Vegas but... before I was 18! So I couldn't touch any of the casinos... Las Vegas is a very shiny place with some good food! I recommend visiting Serendipity for iced hot chocolate."
            },
            {
                "location": "Yellowstone National Park",
                "coordinates": [44.423691, -110.588516],
                "desc": "Yellowstone National Park is very cool. The whole park has so many thermal pools that are the most beautiful shade of blue. Our tour guide actually lost his hat in one of the pools (he did not get it back)!"
            }
        ]
    },
    'mia': {
        "first": "Mia",
        "last": "Yan",
        "github": "https://github.com/yanbmia",
        "linkedin": "https://www.linkedin.com/in/yanbmia/",
        "resume": "",
        "about": "Hey, I'm Mia Yan. I'm a incoming sophmore at Binghamton University studying computer science.",
        "image": "",
        "education": [
            {
                "institution": "Binghamton University",
                "grad_date": "May 2025",
                "courses": "Computer Science",
            }
        ],
        "experience": [
            {
                "position": "Operations Intern",
                "company": "Xenon Health, Inc.",
                "dates": "July 2021 - November 2021",
                "desc": " blah blah ",
            }
        ],
        "hobbies": [
            
        ],
        "locations": [
            {
                "location": "London, UK",
                "coordinates": [51.506180, -0.120142],
                "desc": "I swear summer doesn't exist in London. And yes, I will continue to call the Underground the subway."
            },
            {
                "location": "Rainham, UK",
                "coordinates": [51.366388, 0.611494],
                "desc": "My aunt and cousin moved here in 2019, so of course, I had to visit. (And by visit I totally don't mean I didn't want to pay hotel fees.)"
            },
            {
                "location": "Trinidad and Tobago",
                "coordinates": [10.170945, -61.675227],
                "desc": "My mom is from here! I've been here lots of times to see my family."
            },
            {
                "location": "Miami, FL",
                "coordinates": [25.771533, -80.192114],
                "desc": "Went here in August...I've never experienced humidity like this before."
            },
            {
                "location": "Nassau, The Bahamas",
                "coordinates": [25.044149, -77.354166],
                "desc": "The ocean here is unreal. I was on a cruise with my family when I was 12 and we stopped here."
            },
            {
                "location": "Belize",
                "coordinates": [17.507322, -88.203623],
                "desc": "My mom's uncle's wife is from here! The vibes in Belize are spectacular."
            },
            {
                "location": "Hubei, China",
                "coordinates": [30.703383, 111.292291],
                "desc": "I went only went once when I was very little to visit my dad's family. The food was very good though."
            },
            {
                "location": "Shanghai, China",
                "coordinates": [31.241374, 121.457556],
                "desc": "This city is amazing. I really want to go back soon."
            },
            {
                "location": "Montreal, Canada",
                "coordinates": [45.498696, -73.570269],
                "desc": "One morning, I went to have brunch and the waitress asked me what I wanted to order in French, guess you can say I'm a local. *sarcasm ;)"
            },
            {
                "location": "Southampton, NY",
                "coordinates": [40.884612, -72.393004],
                "desc": "Unfortunately, the Hamptons aren't overhyped. It's really fun here in the summer."
            },
            {
                "location": "Boston, MA",
                "coordinates": [42.358876, -71.056763],
                "desc": "When I was a kid, my family used to take a lot of random road trips. But I'm marking Boston down because I have some funny childhood photos here."
            },
        ]
    },
    "rodrigo": {
        "first": "Rodrigo",
        "last": "",
        "github": "",
        "linkedin": "",
        "resume": "",
        "about": "",
        "image": "",
        "education": [
            {
                "institution": "",
                "grad_date": "",
                "courses": ""
            }
        ],
        "experience": [
            {
                "position": "",
                "company": "",
                "dates": "",
                "desc": "",
            }
        ],
        "hobbies": [
            {
                "name": "",
                "image": "",
                "desc": ""
            },
            {
                "name": "",
                "image": "",
                "desc": "",
            },
            {
                "name": "",
                "image": "",
                "desc": ""
            }
        ],
        "locations": [

        ]
    },
    "kelly": {
        "first": "Kelly",
        "last": "",
        "github": "",
        "linkedin": "",
        "resume": "",
        "about": "",
        "image": "",
        "education": [
            {
                "institution": "",
                "grad_date": "",
                "courses": ""
            }
        ],
        "experience": [
            {
                "position": "",
                "company": "",
                "dates": "",
                "desc": "",
            }
        ],
        "hobbies": [
            {
                "name": "",
                "image": "",
                "desc": ""
            },
            {
                "name": "",
                "image": "",
                "desc": "",
            },
            {
                "name": "",
                "image": "",
                "desc": ""
            }
        ],
        "locations": [

        ]
    },
}

load_dotenv()
app = Flask(__name__)

# home page route
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# fellow's pages route
# input the dictionary of a fellow's information using fellows[name]
@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

@app.route('/map')
def show_map():
    return render_template('map.html', title="Travel", fellows=fellows)
