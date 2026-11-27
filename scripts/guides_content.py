"""Copy for the /help/ guide pages. One entry per category, Hebrew and English written
separately (neither is a translation of the other).

Rules for anything added here:
  - Only claims that are true of the app TODAY (free, phone verification, approximate
    location, report/block, no background checks). No user names, no counts, no quotes
    from real posts - this repo is public.
  - Third-person copy about a user keeps the slash (שכן/ה); direct address uses the
    plural, like the home page.
  - A category gets a page only when it is live in the app's picker. An entry with
    "kind": "guide" (volunteering) is not a category: it is listed in its own hub section.
Build: python3 scripts/build_guides.py
"""

SHARED_FAQ = {
    "he": [
        ("זה עולה כסף?",
         "לא. ההורדה והשימוש בחינם, והעזרה בין השכנים היא בלי תשלום."),
        ("מי רואה את הכתובת שלי?",
         "בפוסט מוצגים אזור משוער ומרחק, אף פעם לא כתובת. המיקום המדויק נחשף רק לשכן/ה שאישרתם."),
        ("איך יודעים שזה בטוח?",
         "לפני שפונים לשכן/ה, מאמתים מספר טלפון. בפרופיל רואים דירוגים וביקורות, "
         "ואפשר לדווח ולחסום בלחיצה. אנחנו לא בודקים רקע של משתמשים, אז ההחלטה להיפגש היא תמיד שלכם."),
    ],
    "en": [
        ("Does it cost anything?",
         "No. The app is free, and help between neighbors is never paid."),
        ("Who can see where I live?",
         "Posts show a rough area and a distance, never an address. Your exact location is only "
         "shared with the neighbor you approve."),
        ("Is it safe?",
         "Before you reach out to a neighbor, you verify your phone number. "
         "Profiles carry ratings and reviews, and you can report or block anyone in one tap. "
         "We don't run background checks, so whether to meet is always your call."),
    ],
}

STEPS = {
    "he": [
        ("מורידים ונרשמים", "Helpy חינמית לאייפון ולאנדרואיד. נרשמים עם Google, ובאייפון גם עם Apple."),
        ("מפרסמים או מגלים", "כותבים מה צריך, או גוללים ורואים מי בסביבה מציע עזרה."),
        ("מתאמים בצ'אט", "קובעים איפה ומתי, נפגשים, ובסוף מדרגים זה את זה."),
    ],
    "en": [
        ("Download Helpy", "It's free on iPhone and Android. Sign in with Google, or with Apple on iPhone."),
        ("Post or browse", "Say what you need, or scroll to see who nearby is offering help."),
        ("Sort it out in chat", "Agree on where and when, meet up, then rate each other."),
    ],
}

# order = order on the hub page
CATEGORIES = [
    {
        "slug": "handyman",
        "he": {
            "label": "הנדימן",
            "title": "הנדימן מהשכונה, בחינם: עזרה בתיקונים קטנים בבית | Helpy",
            "description": "מדף לתלות, ארון להרכיב, ברז שמטפטף. שכנים עם כלים וידיים טובות מציעים עזרה בתיקונים קטנים, בחינם, ב-Helpy.",
            "h1": "הנדימן מהשכונה, לתיקונים הקטנים בבית",
            "lede": "מדף שצריך לתלות, ברז שמטפטף, ארון מאיקאה שעדיין בקרטון. עבודות כאלה לא מצדיקות בעל מקצוע, "
                    "אבל קשה לעשות אותן לבד. ב-Helpy יש שכנים עם כלים וידיים טובות שמציעים לעזור, כמה רחובות מכם.",
            "examples": ["תליית מדפים, תמונות וטלוויזיה", "הרכבת רהיטים", "החלפת ידית, מנעול או נורה גבוהה",
                         "תיקון קטן בברז או בניאגרה"],
            "tips": ["חשמל, גז ואינסטלציה רצינית: רק בעל מקצוע מוסמך.",
                     "צלמו את הבעיה והוסיפו לבקשה, כך השכן/ה יודע/ת מה להביא.",
                     "כתבו אם יש לכם כלים בבית, או שצריך להביא."],
            "faq": [("העזרה בתשלום?",
                     "לא. העזרה ב-Helpy היא בהתנדבות. חומרים, כמו ברגים או ברז חדש, קונים בדרך כלל אתם."),
                    ("ואם התיקון לא החזיק?",
                     "Helpy לא נותנת אחריות על עבודה. לתיקון שצריך עליו אחריות, הזמינו בעל מקצוע.")],
        },
        "en": {
            "label": "Handyman",
            "title": "A handy neighbor for small jobs around the house | Helpy",
            "description": "A shelf to hang, a wardrobe to assemble, a dripping tap. Neighbors with tools offer a hand with small home jobs, free, on Helpy.",
            "h1": "A handy neighbor for the small jobs",
            "lede": "The shelf that's been leaning against the wall for a month. The flat-pack wardrobe still in its box. "
                    "Too small to call someone in, too awkward to do alone. On Helpy, neighbors who own a drill and know "
                    "what to do with it offer to help, a few streets away.",
            "examples": ["Hanging shelves, pictures or a TV", "Putting furniture together",
                         "Swapping a handle, a lock or a bulb you can't reach", "A small fix on a tap or toilet"],
            "tips": ["Electrics, gas and real plumbing are for a licensed pro.",
                     "Add a photo of the problem so your neighbor knows what to bring.",
                     "Say whether you have tools at home or they should bring theirs."],
            "faq": [("Do helpers get paid?",
                     "No. People offer help on Helpy as volunteers. You usually buy the parts, like screws or a new tap."),
                    ("What if the fix doesn't hold?",
                     "Helpy doesn't guarantee anyone's work. If you need a warranty, hire a professional.")],
        },
    },
    {
        "slug": "elderly-care",
        "he": {
            "label": "עזרה לקשישים",
            "title": "עזרה לקשישים בהתנדבות, מהשכנים שגרים קרוב | Helpy",
            "description": "קניות, ביקור, עזרה עם הטלפון או ליווי לתור. שכנים מציעים עזרה לקשישים שגרים קרוב, בחינם, ב-Helpy.",
            "h1": "עזרה לקשישים בהתנדבות, מהשכנים שגרים קרוב",
            "lede": "קניות לסבתא שלא יוצאת הרבה, ביקור קבוע אצל שכן מבוגר שגר לבד, עזרה עם הטלפון או עם טופס. "
                    "ב-Helpy יש שכנים שמחפשים דרך לתת מהזמן שלהם, ורבים מהם בוחרים דווקא בזה.",
            "examples": ["קניות בסופר או בבית המרקחת", "ביקור ושיחה, פעם בשבוע",
                         "עזרה עם הטלפון, וואטסאפ או זימון תור", "ליווי לבדיקה או לסידורים"],
            "tips": ["בני משפחה יכולים לפרסם בקשה בשם ההורים, ולהיות אלה שמתאמים בצ'אט.",
                     "בפגישה הראשונה כדאי שעוד מישהו מהמשפחה יהיה שם.",
                     "לא מוסרים לאף אחד כרטיס אשראי, קוד או סיסמה."],
            "faq": [("ההורים שלי לא מסתדרים עם אפליקציות. אפשר לבקש בשבילם?",
                     "כן, כשהם גרים קרוב אליכם. מפרסמים מהטלפון שלכם, כותבים בבקשה מה הם צריכים, ומתאמים בצ'אט. הבקשה מוצגת לשכנים סביב המיקום שלכם באפליקציה."),
                    ("זה מחליף מטפל או מטפלת?",
                     "לא. שכנים עוזרים במשימות קטנות ובחברה. טיפול אישי וסיעודי הם עבודה של אנשי מקצוע.")],
        },
        "en": {
            "label": "Elderly care",
            "title": "Volunteer help for older neighbors, from people nearby | Helpy",
            "description": "Groceries, a weekly visit, help with a phone or getting to an appointment. Neighbors offer free help to older people close by, on Helpy.",
            "h1": "Help for older neighbors, from people who live nearby",
            "lede": "Groceries for a grandmother who doesn't get out much. A regular visit to the man upstairs who lives alone. "
                    "Someone patient enough to explain WhatsApp. Plenty of people on Helpy want to give some of their time, "
                    "and many of them choose exactly this.",
            "examples": ["Groceries or a pharmacy run", "A visit and a chat, once a week",
                         "Help with a phone, WhatsApp or booking an appointment", "Company on the way to a check-up"],
            "tips": ["Family can post on a parent's behalf and handle the chat themselves.",
                     "For the first meeting, it helps if a relative is there too.",
                     "Never hand over a bank card, a code or a password."],
            "faq": [("My parents don't use apps. Can I ask for them?",
                     "Yes, if they live near you. Post from your phone, say what they need, and handle the chat yourself. The request is shown to neighbors around your own location in the app."),
                    ("Is this a replacement for a carer?",
                     "No. Neighbors help with small tasks and company. Personal and nursing care is work for professionals.")],
        },
    },
    {
        "slug": "tech-help",
        "he": {
            "label": "עזרה במחשב",
            "title": "עזרה במחשבים ובטלפון בחינם, גם למבוגרים | Helpy",
            "description": "טלפון חדש להגדיר, מדפסת שלא מתחברת, אפליקציה להתקין. שכנים שמבינים במחשבים מציעים עזרה בחינם, ב-Helpy.",
            "h1": "עזרה במחשב ובטלפון בחינם, משכנים שמבינים בזה",
            "lede": "טלפון חדש שצריך להעביר אליו את התמונות, מדפסת שהפסיקה להתחבר, זום שלא מצליחים להיכנס אליו. "
                    "בדרך כלל זה עניין של חצי שעה עם מישהו שמבין. ב-Helpy השכנים האלה גרים קרוב ומציעים לעזור.",
            "examples": ["להגדיר טלפון חדש ולהעביר אליו תמונות ואנשי קשר", "מדפסת או ראוטר שלא מתחברים",
                         "להתקין אפליקציה או לעדכן את המחשב", "ללמוד להשתמש בזום, בוואטסאפ או בג'ימייל"],
            "tips": ["אל תמסרו סיסמאות, קודים שמגיעים ב-SMS או פרטי אשראי, גם לא לשכן/ה נחמד/ה.",
                     "עדיף שהעזרה תהיה מול העיניים שלכם, ולא בהשתלטות מרחוק.",
                     "לפני שמתקנים משהו, מגבים את מה שחשוב."],
            "faq": [("אפשר לקבל עזרה בשיחת וידאו?",
                     "רוב העזרה ב-Helpy היא פנים אל פנים, בין שכנים קרובים. אם שניכם מעדיפים וידאו, מתאמים את זה בצ'אט."),
                    ("המחשב ממש מקולקל. זה המקום?",
                     "לתקלת חומרה או לשחזור מידע עדיף טכנאי. שכנים עוזרים בעיקר בהגדרות, בהתקנות ובהסברים.")],
        },
        "en": {
            "label": "Tech help",
            "title": "Computer and phone help from a neighbor who gets it | Helpy",
            "description": "A new phone to set up, a printer that won't connect, an app to install. Tech-savvy neighbors help for free, on Helpy.",
            "h1": "Computer and phone help, from a neighbor who gets it",
            "lede": "A new phone that needs your photos moved over. A printer that stopped talking to the Wi-Fi. "
                    "A Zoom link that just won't open. Usually it's half an hour with someone who knows. "
                    "On Helpy, those people live nearby and offer to help.",
            "examples": ["Setting up a new phone and moving photos and contacts", "A printer or router that won't connect",
                         "Installing an app or updating a computer", "Learning Zoom, WhatsApp or Gmail"],
            "tips": ["Never share passwords, SMS codes or card details, not even with a nice neighbor.",
                     "Keep the help in front of you rather than handing over remote control.",
                     "Back up anything important before anyone fixes anything."],
            "faq": [("Can someone help over a video call?",
                     "Most help on Helpy happens in person, between people who live close. If you both prefer video, arrange it in the chat."),
                    ("My computer is properly broken. Is this the place?",
                     "For hardware faults or data recovery, go to a technician. Neighbors mostly help with settings, installs and explaining.")],
        },
    },
    {
        "slug": "giveaway",
        "he": {
            "label": "מסירה",
            "title": "למסירה בחינם בשכונה: רהיטים, ציוד לתינוקות ועוד | Helpy",
            "description": "ארון, עגלה, ספרים או כלי מטבח. מוסרים בחינם לשכנים קרובים, או מבקשים משהו שחסר, ב-Helpy.",
            "h1": "למסירה בחינם, לשכנים שגרים קרוב",
            "lede": "ארון שלא נכנס בדירה החדשה, עגלה שכבר לא צריך, ספרים שאף אחד לא קורא. "
                    "במקום לזרוק, מפרסמים במסירה ב-Helpy והשכנים הקרובים רואים את זה. ואם מחפשים משהו, אפשר גם לבקש.",
            "examples": ["רהיטים: ארון, שולחן, כיסאות", "ציוד לתינוקות ולילדים",
                         "ספרים, משחקים וכלי מטבח", "מכשירי חשמל קטנים שעובדים"],
            "tips": ["צלמו את החפץ, וכתבו מידות ומצב בכנות.",
                     "קבעו איסוף בכניסה לבניין או במקום ציבורי.",
                     "מסירה היא בחינם. על בקשה לכסף אפשר לדווח מהאפליקציה."],
            "faq": [("מי מקבל את החפץ?",
                     "אתם בוחרים. רואים מי פנה, מדברים בצ'אט, ומוסרים למי שמתאים לכם."),
                    ("אפשר גם למכור?",
                     "לא. Helpy היא לעזרה ולמסירה בחינם. למכירה יש מקומות אחרים.")],
        },
        "en": {
            "label": "Giveaway",
            "title": "Free stuff near you: give away or ask your neighbors | Helpy",
            "description": "A wardrobe, a stroller, books or kitchenware. Give things away free to people nearby, or ask for something you need, on Helpy.",
            "h1": "Give it away to someone down the street",
            "lede": "The wardrobe that didn't fit in the new place. A stroller you're done with. A shelf of books nobody reads. "
                    "Rather than bin them, post them on Helpy and the people closest to you see them first. "
                    "Looking for something? You can ask, too.",
            "examples": ["Furniture: wardrobes, tables, chairs", "Baby and kids' gear",
                         "Books, games and kitchenware", "Small appliances that still work"],
            "tips": ["Add a photo, and be honest about size and condition.",
                     "Arrange pickup at the building entrance or somewhere public.",
                     "Giveaways are free. If someone asks for money, you can report them in the app."],
            "faq": [("Who gets the item?",
                     "You decide. See who reached out, chat with them, and pick who it goes to."),
                    ("Can I sell things on Helpy?",
                     "No. Helpy is for help and free giveaways. For selling, use somewhere else.")],
        },
    },
    {
        "slug": "borrow",
        "he": {
            "label": "השאלה",
            "title": "השאלת כלים וציוד מהשכנים, במקום לקנות | Helpy",
            "description": "מקדחה, סולם, אוהל או מזוודה. משאילים מהשכנים הקרובים ומחזירים בסוף, בחינם, ב-Helpy.",
            "h1": "השאלת כלים וציוד מהשכנים, במקום לקנות",
            "lede": "מקדחה בשביל מדף אחד, סולם גבוה לפעם בשנה, מזוודה גדולה לטיסה, אוהל לסוף שבוע. "
                    "רוב הדברים האלה עומדים במחסן של מישהו כמה בניינים מכם. ב-Helpy מבקשים, משאילים ומחזירים.",
            "examples": ["מקדחה, סולם או ארגז כלים", "ציוד קמפינג ומזוודות",
                         "לול, עגלה או כיסא בטיחות לנכדים שבאים לביקור", "תבניות ומגשים לאירוח גדול"],
            "tips": ["סכמו מראש מתי מחזירים.", "צלמו את החפץ כשאתם מקבלים אותו.",
                     "החזירו נקי, ובמצב שבו קיבלתם."],
            "faq": [("ומה אם משהו נשבר?",
                     "מדברים על זה בצ'אט לפני ההשאלה. Helpy מחברת בין שכנים ולא מבטחת חפצים, אז כדאי לסכם מראש מה עושים אם קורה משהו."),
                    ("אפשר להציע להשאיל?",
                     "כן. מפרסמים הצעה, למשל \"יש לי מקדחה, מי שצריך מוזמן\", ושכנים פונים כשהם צריכים.")],
        },
        "en": {
            "label": "Borrow",
            "title": "Borrow from neighbors instead of buying | Helpy",
            "description": "A drill, a ladder, a tent or a suitcase. Borrow from people nearby and give it back after, free, on Helpy.",
            "h1": "Borrow it from a neighbor instead of buying it",
            "lede": "A drill for one shelf. A tall ladder once a year. A big suitcase for one trip, a tent for one weekend. "
                    "Most of these are sitting in a storeroom a few buildings away. On Helpy you ask, borrow, and bring it back.",
            "examples": ["A drill, a ladder or a toolbox", "Camping gear and suitcases",
                         "A travel cot, stroller or car seat for visiting grandkids", "Baking trays and platters for a big gathering"],
            "tips": ["Agree on a return date up front.", "Take a photo of the item when you pick it up.",
                     "Give it back clean, in the state you got it."],
            "faq": [("What if something breaks?",
                     "Talk about it in the chat before you borrow. Helpy connects neighbors and doesn't insure anything, so agree on what happens if something goes wrong."),
                    ("Can I offer to lend things?",
                     "Yes. Post an offer, something like \"I have a drill, just ask\", and neighbors get in touch when they need it.")],
        },
    },
    {
        "slug": "tutoring",
        "he": {
            "label": "שיעורי עזר",
            "title": "שיעורי עזר בחינם מהשכנים, בהתנדבות | Helpy",
            "description": "מתמטיקה, אנגלית, הכנה לבגרות או עזרה באקסל. שכנים מציעים שיעורי עזר בחומר שהם מכירים, בחינם, ב-Helpy.",
            "h1": "שיעורי עזר מהשכנים, בהתנדבות",
            "lede": "ילד שנתקע בשברים, תלמידה לפני בגרות באנגלית, מבוגר שרוצה סוף סוף להבין אקסל. "
                    "ב-Helpy יש שכנים שמציעים לעזור בחומר שהם מכירים, בהתנדבות ובלי מחירון.",
            "examples": ["מתמטיקה ואנגלית ליסודי ולחטיבה", "הכנה למבחן או לבגרות",
                         "עזרה בכתיבת עבודה או קורות חיים", "אקסל, מצגות ותוכנות"],
            "tips": ["בשיעור לילדים, הורה נמצא בבית, או שהשיעור במקום ציבורי כמו ספרייה.",
                     "כתבו כיתה, מקצוע ונושא, כך יפנו מי שמתאימים.",
                     "פגישה ראשונה קצרה עוזרת לראות אם יש חיבור."],
            "faq": [("השיעורים בתשלום?",
                     "לא. ב-Helpy שכנים עוזרים בהתנדבות. מורים פרטיים בתשלום מוצאים במקומות אחרים."),
                    ("אני רוצה לעזור, אבל אני לא מורה.",
                     "לא צריך תעודה. אם אתם טובים במשהו, מפרסמים הצעה עם המקצוע והגיל, ושכנים שצריכים יפנו.")],
        },
        "en": {
            "label": "Tutoring",
            "title": "Free tutoring from neighbors | Helpy",
            "description": "Maths, English, exam prep or Excel. Neighbors offer to tutor in what they know, as volunteers, on Helpy.",
            "h1": "Tutoring from the neighbors, for free",
            "lede": "A kid stuck on fractions. A student a month out from an English exam. An adult who'd finally like to get Excel. "
                    "On Helpy, neighbors offer to help with what they know, as volunteers, with no price list.",
            "examples": ["Maths and English for primary and middle school", "Getting ready for a test or a final exam",
                         "Help with an essay or a CV", "Excel, slides and other software"],
            "tips": ["For a child's lesson, a parent stays home, or meet somewhere public like a library.",
                     "Say the grade, the subject and the topic so the right people reach out.",
                     "A short first session shows whether it clicks."],
            "faq": [("Are the lessons paid?",
                     "No. On Helpy neighbors help as volunteers. For a paid private tutor, look elsewhere."),
                    ("I'd like to help, but I'm not a teacher.",
                     "You don't need a certificate. If you're good at something, post an offer with the subject and age group, and people who need it will reach out.")],
        },
    },
    {
        "slug": "moving",
        "he": {
            "label": "הובלות",
            "title": "עזרה בהובלה בחינם: שכנים עוזרים לסחוב | Helpy",
            "description": "ספה לקומה שלישית, קרטונים למחסן, עוד זוג ידיים ביום המעבר. שכנים מציעים עזרה בסחיבה, בחינם, ב-Helpy.",
            "h1": "עזרה בהובלה ובסחיבה, מהשכנים",
            "lede": "ספה שצריך להעלות לקומה שלישית בלי מעלית, ארונות שצריך להוריד למחסן, דירה קטנה שעוברת שני רחובות. "
                    "בשביל עשר דקות של סחיבה לא תמיד מזמינים מובילים. ב-Helpy מבקשים מהשכנים הקרובים, "
                    "ומי שיכול/ה מציע/ה לעזור.",
            "examples": ["להעלות ספה או מקרר לקומה בלי מעלית", "להוריד קרטונים למחסן או לרכב",
                         "עוד זוג ידיים ביום המעבר", "להעביר שולחן או מזרן לרחוב ליד"],
            "tips": ["כתבו כמה פריטים יש, באיזו קומה, ואם יש מעלית.",
                     "פסנתר, כספת וכל דבר כבד במיוחד: מובילים מקצועיים.",
                     "סכמו שעה בצ'אט, ושתפו אותה עם מישהו קרוב."],
            "faq": [("מה אם אף אחד לא עונה?",
                     "אפשר לשתף את הבקשה מהאפליקציה לקבוצת השכונה בוואטסאפ או בפייסבוק, וכך עוד שכנים יראו אותה."),
                    ("זה מחליף חברת הובלות?",
                     "לא לדירה שלמה. שכנים עוזרים בסחיבות קצרות ובפריטים בודדים.")],
        },
        "en": {
            "label": "Moving",
            "title": "Help moving and lifting, from neighbors | Helpy",
            "description": "A sofa up three flights, boxes down to storage, an extra pair of hands on moving day. Neighbors help with the heavy lifting, free, on Helpy.",
            "h1": "An extra pair of hands for the heavy lifting",
            "lede": "A sofa that has to go up three floors with no lift. Wardrobes that need to come down to storage. "
                    "A small flat moving two streets over. Nobody books movers for ten minutes of carrying. "
                    "On Helpy you ask the people closest to you, and whoever has the time and the muscle offers to help.",
            "examples": ["Getting a sofa or fridge up the stairs", "Carrying boxes down to storage or a car",
                         "An extra pair of hands on moving day", "Moving a table or mattress to the next street"],
            "tips": ["Say how many items, which floor, and whether there's a lift.",
                     "Pianos, safes and anything really heavy: book professional movers.",
                     "Agree on a time in the chat, and let someone close to you know."],
            "faq": [("What if nobody answers?",
                     "Share the post from the app to your neighborhood WhatsApp or Facebook group so more people see it."),
                    ("Can this replace a moving company?",
                     "Not for a whole flat. Neighbors help with short carries and single items.")],
        },
    },
    {
        # app category key: "transportation" (older posts) / "rides"; both are labelled טרמפ / Rides
        "slug": "rides",
        "he": {
            "label": "טרמפ",
            "title": "טרמפים בשכונה: נסיעה משותפת עם שכנים | Helpy",
            "description": "לרכבת בבוקר, לבדיקה בבית החולים, או להעביר משהו גדול. שכנים שנוסעים בכל מקרה מציעים מקום ברכב, ב-Helpy.",
            "h1": "טרמפ מהשכנים, למי שבדרך",
            "lede": "צריך להגיע לרכבת מוקדם בבוקר, לבדיקה בבית החולים, או להעביר משהו גדול לעיר ליד? "
                    "אולי שכן/ה נוסע/ת לשם בכל מקרה. ב-Helpy מפרסמים לאן ומתי, ומי שבדרך מציע/ה מקום ברכב.",
            "examples": ["הסעה לרכבת או לתחנה המרכזית", "נסיעה לבדיקה או לתור",
                         "שכנים שנוסעים כל בוקר לאותו אזור", "העברת חבילה או חפץ גדול ברכב"],
            "tips": ["שתפו עם מישהו קרוב לאן אתם נוסעים, עם מי ומתי.",
                     "בדקו בפרופיל דירוגים וביקורות.",
                     "סכמו בצ'אט נקודת איסוף ברורה."],
            "faq": [("Helpy היא שירות הסעות?",
                     "לא. אין נהגים מקצועיים, יש שכנים שנוסעים בכל מקרה ומציעים מקום."),
                    ("מתי כדאי לפרסם?",
                     "כמה שיותר מראש, כדי שלשכנים יהיה זמן לראות ולתאם.")],
        },
        "en": {
            "label": "Rides",
            "title": "Rides from neighbors who are going your way | Helpy",
            "description": "To the train in the morning, to a hospital appointment, or to move something bulky. Neighbors already heading there offer a seat, on Helpy.",
            "h1": "A lift from a neighbor who's going that way anyway",
            "lede": "An early train to catch, a hospital appointment, something too big for the bus. "
                    "Someone on your street might be heading there anyway. On Helpy you post where and when, "
                    "and whoever's going that way offers a seat.",
            "examples": ["A lift to the train or bus station", "Getting to a check-up or appointment",
                         "Neighbors who commute to the same area every morning", "Moving a parcel or something bulky by car"],
            "tips": ["Tell someone close to you where you're going, with whom, and when.",
                     "Check the driver's ratings and reviews on their profile.",
                     "Agree on a clear pickup point in the chat."],
            "faq": [("Is Helpy a ride service?",
                     "No. There are no professional drivers, just neighbors who are making the trip anyway and have a free seat."),
                    ("When should I post?",
                     "As early as you can, so neighbors have time to see it and plan.")],
        },
    },
    {
        "slug": "pets",
        "he": {
            "label": "חיות מחמד",
            "title": "שמירה על כלב וטיולים בעזרת השכנים | Helpy",
            "description": "טיול צהריים לכלב, האכלת חתול בסוף השבוע, הסעה לווטרינר. שכנים שאוהבים חיות מציעים עזרה, בחינם, ב-Helpy.",
            "h1": "שמירה על הכלב, טיולים ועזרה עם חיות המחמד, משכנים",
            "lede": "טיול צהריים לכלב כשאתם בעבודה, מישהו שיאכיל את החתול בסוף השבוע, עזרה להביא את הכלב לווטרינר. "
                    "ב-Helpy יש שכנים שאוהבים חיות ומציעים לעזור, קרוב לבית.",
            "examples": ["טיולים עם הכלב", "האכלת חתול או דגים כשאתם לא בבית",
                         "הסעה לווטרינר", "עצה מבעלי חיים מנוסים"],
            "tips": ["פגישת היכרות קצרה עם החיה, לפני הפעם הראשונה.",
                     "השאירו הוראות כתובות ומספר של וטרינר.",
                     "מפתח לבית: רק למי שאתם מכירים וסומכים עליו/ה."],
            "faq": [("זה פנסיון?",
                     "לא. שכנים עוזרים לזמן קצר. לשהייה ארוכה או לטיפול רפואי, פנו לפנסיון או לווטרינר."),
                    ("אני רוצה לעזור עם כלבים בשכונה.",
                     "מפרסמים הצעת עזרה בקטגוריית חיות מחמד, ובעלי כלבים קרובים יפנו.")],
        },
        "en": {
            "label": "Pets",
            "title": "Pet help from neighbors who love animals | Helpy",
            "description": "A midday dog walk, feeding the cat over the weekend, a lift to the vet. Animal-loving neighbors offer help, free, on Helpy.",
            "h1": "Help with your pets, from neighbors who love animals",
            "lede": "A midday walk while you're at work. Someone to feed the cat over the weekend. "
                    "A hand getting a nervous dog to the vet. On Helpy, animal people a few doors down offer to help.",
            "examples": ["Dog walks", "Feeding a cat or fish while you're away",
                         "A lift to the vet", "Advice from experienced owners"],
            "tips": ["Do a short meet-and-greet with your pet before the first time.",
                     "Leave written instructions and your vet's number.",
                     "Only give a house key to someone you know and trust."],
            "faq": [("Is this a boarding service?",
                     "No. Neighbors help for short stretches. For long stays or medical care, use a kennel or a vet."),
                    ("I'd like to help with dogs in my area.",
                     "Post an offer in the Pets category, and dog owners nearby will reach out.")],
        },
    },
    {
        "slug": "volunteer",
        "kind": "guide",  # not an app category: own hub section, not listed among categories
        "he": {
            "label": "התנדבות ליד הבית",
            "title": "התנדבות ליד הבית: לעזור לשכנים כשיש לכם זמן | Helpy",
            "description": "רוצים להתנדב בלי קורס ובלי משמרת קבועה? ב-Helpy רואים מי בשכונה צריך עזרה, ועוזרים כשזה מתאים לכם. בחינם.",
            "h1": "התנדבות ליד הבית, כשיש לכם זמן",
            "lede": "לא כל התנדבות צריכה קורס, ראיון ומשמרת קבועה. לפעמים זה לסחוב ספה עם שכן, לעזור לשכנה מבוגרת עם הטלפון, "
                    "או להסביר לילד שברים. ב-Helpy רואים מה צריכים השכנים שגרים קרוב, ומציעים עזרה רק כשזה מתאים לכם.",
            "examples": ["קניות, ביקור או עזרה עם הטלפון לשכנים מבוגרים", "סחיבה, הרכבה ותיקונים קטנים",
                         "שיעורי עזר במקצוע שאתם טובים בו", "טרמפ למי שבדרך שלכם"],
            "tips": ["מתחילים במשהו קטן וקרוב. בזה הכי קל להתמיד.",
                     "אפשר גם לפרסם הצעה: במה אתם יכולים לעזור, ושכנים יפנו אליכם.",
                     "מחפשים מסגרת קבועה עם הכשרה וליווי? עיריות ועמותות מפעילות תוכניות כאלה, ו-Helpy לא מחליפה אותן."],
            "faq": [("צריך להתחייב?",
                     "לא. עוזרים כשיש זמן, ובוחרים למי להציע עזרה."),
                    ("זו התנדבות רשמית?",
                     "לא. Helpy היא קהילה של שכנים, לא ארגון מתנדבים, ואין בה אישורים או שעות התנדבות.")],
        },
        "en": {
            "label": "Volunteer near home",
            "title": "Volunteer near home, whenever you have time | Helpy",
            "description": "Want to volunteer without a course or a fixed shift? On Helpy you see who nearby needs a hand and help when it suits you. Free.",
            "h1": "Volunteer on your own street, on your own time",
            "lede": "Not every way of giving back needs an induction, an interview and a weekly shift. Sometimes it's carrying a sofa "
                    "with the guy downstairs, sorting out a phone for the woman next door, or walking a kid through fractions. "
                    "Helpy shows you what the people around you need, and you offer when it works for you.",
            "examples": ["Groceries, a visit or phone help for older neighbors", "Carrying, assembling and small fixes",
                         "Tutoring in a subject you're good at", "A lift for someone going your way"],
            "tips": ["Start with something small and close by. That's what people keep doing.",
                     "You can post an offer too: say what you can help with, and neighbors will reach out.",
                     "Want a structured program with training? Cities and charities run those, and Helpy doesn't replace them."],
            "faq": [("Do I have to commit to anything?",
                     "No. Help when you have time, and choose who you offer to help."),
                    ("Does this count as formal volunteering?",
                     "No. Helpy is a community of neighbors, not a volunteer organization, so there are no certificates or logged hours.")],
        },
    },
]

HUB = {
    "he": {
        "title": "במה שכנים עוזרים זה לזה | Helpy",
        "description": "הנדימן, עזרה לקשישים, מסירה, השאלה, שיעורי עזר, טרמפים ועוד. כל הדרכים שבהן שכנים עוזרים זה לזה ב-Helpy, בחינם.",
        "h1": "במה שכנים עוזרים זה לזה",
        "lede": "ב-Helpy מבקשים עזרה מהשכנים שגרים קרוב, או מציעים אותה. אלה הדברים שהכי הרבה אנשים מבקשים ומציעים.",
    },
    "en": {
        "title": "What neighbors help each other with | Helpy",
        "description": "Handyman jobs, help for older neighbors, giveaways, borrowing, tutoring, rides and more. Every way neighbors help each other on Helpy, for free.",
        "h1": "What neighbors help each other with",
        "lede": "On Helpy you ask the people who live nearby for a hand, or offer one. These are the things people ask for and offer most.",
    },
}


# City pages: cities with >= 30 real (non-test) posts in the last 120 days, snapshot 27.11.2026.
# `cats` = categories with a guide page, most posted first. `offers_majority` = most posts there in that
# window were offers (the lede says so only when True). Aggregate only: no counts, names or post text.
# Refresh: count posts per city and per category over the last 120 days, excluding test accounts.
CITIES_ASOF = {"he": "נובמבר 2026", "en": "November 2026"}
CITIES = [
    {"slug": "tel-aviv", "offers_majority": True, "he": "תל אביב-יפו", "en": "Tel Aviv-Yafo",
     "cats": ["handyman", "elderly-care", "giveaway", "tech-help", "tutoring", "borrow"]},
    {"slug": "petah-tikva", "offers_majority": True, "he": "פתח תקווה", "en": "Petah Tikva",
     "cats": ["handyman", "tech-help", "giveaway", "tutoring", "elderly-care"]},
    {"slug": "ramat-gan", "offers_majority": True, "he": "רמת גן", "en": "Ramat Gan",
     "cats": ["handyman", "giveaway", "tech-help", "pets", "tutoring"]},
    {"slug": "holon", "offers_majority": True, "he": "חולון", "en": "Holon",
     "cats": ["handyman", "elderly-care", "tutoring", "giveaway"]},
    {"slug": "netanya", "offers_majority": True, "he": "נתניה", "en": "Netanya",
     "cats": ["elderly-care", "handyman", "tech-help", "rides", "giveaway"]},
]

CITY_COPY = {
    "he": {
        "title": "עזרה משכנים והתנדבות ב{city} | Helpy",
        "description": "שכנים ב{city} מבקשים ומציעים עזרה: תיקונים, מסירה, עזרה לקשישים ועוד. בחינם, באפליקציית Helpy.",
        "h1": "שכנים עוזרים לשכנים ב{city}",
        "lede": "ב-Helpy שכנים ב{city} מבקשים עזרה ומציעים אותה, ברחוב שלהם.",
        "offers": "בחודשים האחרונים רוב הפוסטים בעיר היו הצעות עזרה, כלומר יש פה שכנים שמחכים שמישהו יבקש.",
        "cats_h2": "מה מבקשים ומציעים ב{city}",
        "cats_note": "לפי הפוסטים בעיר בחודשים האחרונים, נכון ל{asof}.",
        "vol_h2": "להתנדב ב{city}, ליד הבית",
        "vol_p": "בלי קורס ובלי משמרת קבועה: רואים מה צריכים השכנים הקרובים, ומציעים עזרה כשמתאים לכם.",
        "vol_link": "איך מתנדבים ב-Helpy",
        "label": "{city}",
    },
    "en": {
        "title": "Neighbors helping neighbors in {city} | Helpy",
        "description": "People in {city} ask for and offer help: small fixes, giveaways, help for older neighbors and more. Free, on the Helpy app.",
        "h1": "Neighbors helping neighbors in {city}",
        "lede": "On Helpy, people in {city} ask for a hand and offer one, on their own streets.",
        "offers": "In recent months most posts in the city were offers, which means there are neighbors here waiting for someone to ask.",
        "cats_h2": "What people in {city} ask for and offer",
        "cats_note": "Based on posts in the city over recent months, as of {asof}.",
        "vol_h2": "Volunteer in {city}, close to home",
        "vol_p": "No course and no fixed shift: see what the people nearby need, and offer when it suits you.",
        "vol_link": "How volunteering on Helpy works",
        "label": "{city}",
    },
}
