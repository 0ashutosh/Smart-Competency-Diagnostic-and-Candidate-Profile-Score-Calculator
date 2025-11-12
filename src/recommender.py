from typing import List, Tuple

# Minimal curated skills bank (add freely)
SKILLBANK = [
    # DS
    "python","pandas","numpy","scikit-learn","tensorflow","keras","pytorch",
    "machine learning","deep learning","sql","matplotlib","seaborn","nlp",
    # Web
    "javascript","react","node","express","django","flask","html","css","typescript",
    # Android
    "android","kotlin","java","xml","jetpack","android studio","flutter",
    # iOS
    "ios","swift","xcode","cocoa","objective-c",
    # UI/UX
    "ui","ux","wireframe","figma","adobe xd","prototyping","user research"
]

DS_COURSES = [
    ("Data Science Specialization (Coursera)", "https://www.coursera.org/specializations/jhu-data-science"),
    ("Intro to ML (fast.ai)", "https://course.fast.ai/")
]
WEB_COURSES = [
    ("The Odin Project (Full Stack)", "https://www.theodinproject.com/"),
    ("Django Official Tutorial", "https://docs.djangoproject.com/en/stable/intro/tutorial01/")
]
ANDROID_COURSES = [
    ("Android Basics (Google)", "https://developer.android.com/courses"),
]
IOS_COURSES = [
    ("Develop in Swift (Apple)", "https://developer.apple.com/tutorials/")
]
UIUX_COURSES = [
    ("Google UX (Coursera)", "https://www.coursera.org/professional-certificates/google-ux-design"),
]

def classify_field(skills: List[str]) -> str:
    s = set(x.lower() for x in skills)
    if {"pytorch","tensorflow","machine learning"} & s:
        return "Data Science"
    if {"react","django","flask","node","javascript"} & s:
        return "Web Development"
    if {"android","kotlin","android studio","flutter"} & s:
        return "Android Development"
    if {"ios","swift","xcode"} & s:
        return "iOS Development"
    if {"ux","ui","figma","wireframe"} & s:
        return "UI/UX"
    return "General"

def recommend_skills(field: str) -> List[str]:
    if field == "Data Science":
        return ["data visualization","feature engineering","model evaluation","ml ops","time series"]
    if field == "Web Development":
        return ["rest apis","auth","orm","testing","docker"]
    if field == "Android Development":
        return ["jetpack compose","room","retrofit","unit testing"]
    if field == "iOS Development":
        return ["swiftui","combine","core data","uikit"]
    if field == "UI/UX":
        return ["user flows","usability testing","design systems","accessibility"]
    return ["git","testing","debugging"]

def recommend_courses(field: str) -> List[Tuple[str,str]]:
    return {
        "Data Science": DS_COURSES,
        "Web Development": WEB_COURSES,
        "Android Development": ANDROID_COURSES,
        "iOS Development": IOS_COURSES,
        "UI/UX": UIUX_COURSES
    }.get(field, [])
