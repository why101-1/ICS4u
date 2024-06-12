from flask import Flask, render_template, url_for, redirect, request
import json
from bson import ObjectId

from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__,static_folder='static')

app.config["MONGO_URI"] = "mongodb+srv://computerscienceics4u:nose321@cluster0.rh1oi0j.mongodb.net/terms"
mongo = PyMongo(app)

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



lists = [
    "DigitalDivide",
    "Cyberbullying",
    "MisinformationandDisinformation",
    "AlgorithmicBias",
    "OnlineRadicalization",
    "NetNeutrality",
    "OnlineCensorshipandFreeSpeech",
    "DigitalAddiction",
    "OnlineScams",
    "OnlineVotingSecurity"
]
try:
    for i in lists:
        mongo.db.create_collection(i)
except :
    print("Error")

def insert_data(collect_name, question, answer):
    collect_name.insert_one({"Question":"What are the underlying causes and contributing factors?", "Answer" :answer})
    
insert_data(mongo.db.DigitalDivide, "What are the underlying causes and contributing factors?", "The digital divide is driven by economic disparities that lead to unequal access to technology and the internet. Contributing factors include income inequality, variations in educational opportunities, and differences in infrastructure development between urban and rural areas. Government policies and corporate interests also play a significant role, with inadequate investment in underserved regions further widening the gap.")
insert_data(mongo.db.Cyberbullying, "What are the underlying causes and contributing factors?","Cyberbullying is fueled by the pervasive use of social media and digital communication platforms that provide anonymity and a broad reach for harassers. Contributing factors include the lack of effective regulation and moderation on these platforms, as well as the social dynamics of peer pressure and competition. The anonymity and perceived distance of online interactions often embolden individuals to engage in behavior they might avoid in face-to-face settings.")
insert_data(mongo.db.MisinformationandDisinformation, "What are the underlying causes and contributing factors?","Misinformation and disinformation spread rapidly due to the democratization of content creation and the algorithms that favor sensational, engaging content. Factors contributing to this issue include the decline in traditional journalism’s gatekeeping role, the rise of social media platforms, and the ease with which false information can be shared. Societal polarization and declining trust in institutions further exacerbate the problem.")
insert_data(mongo.db.AlgorithmicBias, "What are the underlying causes and contributing factors?","Algorithmic bias results from the data used to train AI systems, which often reflect existing societal prejudices and inequalities. Contributing factors include the lack of diversity in the tech industry, insufficient transparency in algorithm development, and the complexity of ensuring fair representation in datasets. These biases are perpetuated when algorithms make decisions based on skewed or incomplete data.")
insert_data(mongo.db.OnlineRadicalization, "What are the underlying causes and contributing factors?","Online radicalization is driven by the internet’s ability to connect like-minded individuals and expose users to extremist ideologies through echo chambers and algorithm-driven content recommendations. Contributing factors include social isolation, political polarization, and the anonymity provided by online platforms. These environments facilitate the spread of radical ideologies to susceptible individuals.")
insert_data(mongo.db.NetNeutrality, "What are the underlying causes and contributing factors?","Net neutrality is challenged by the economic interests of major internet service providers (ISPs) who seek to monetize data traffic by prioritizing certain content or services. Contributing factors include deregulation trends, consolidation in the telecom industry, and the increasing influence of a few tech giants. These factors create an environment where ISPs can potentially undermine the principle of an open and equal internet.")
insert_data(mongo.db.OnlineCensorshipandFreeSpeech, "What are the underlying causes and contributing factors?","Online censorship and free speech issues arise from efforts by governments and corporations to control content for political, moral, or economic reasons. Contributing factors include national security concerns, intellectual property rights, and attempts to curb misinformation and hate speech. The balance between protecting free speech and preventing harmful content is influenced by cultural norms, legal frameworks, and political climates.")
insert_data(mongo.db.DigitalAddiction, "What are the underlying causes and contributing factors?","Digital addiction is driven by the widespread use of technology and the internet, which are designed to capture and retain user attention through engaging and rewarding experiences. Contributing factors include the psychological tactics employed by social media and gaming platforms, such as variable rewards and social validation. The normalization of constant connectivity and the pressure to maintain an online presence exacerbate the problem.")
insert_data(mongo.db.OnlineScams, "What are the underlying causes and contributing factors?","Online scams proliferate due to the anonymity and broad reach of the internet, which allow scammers to target victims across the globe. Contributing factors include the lack of digital literacy among users, insufficient cybersecurity measures, and the sophistication of scam techniques. The rapid evolution of technology often outpaces the ability of individuals and organizations to protect themselves from these threats.")
insert_data(mongo.db.OnlineVotingSecurity,"What are the underlying causes and contributing factors?", "Online voting security issues stem from the inherent vulnerabilities of digital systems, which can be exploited by hackers and malicious actors. Contributing factors include inadequate cybersecurity measures, the complexity of ensuring a secure and anonymous voting process, and the potential for large-scale disruptions. The reliance on technology for critical democratic processes amplifies the need for robust security protocols to maintain trust in electoral outcomes.")


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/transfer", methods= ["GET","POST"])
def returnFile():
    if request.method == "POST":
        data = request.form["data"]
        print("fjdslkfjdsl")
        return "fdsafsd"
    return render_template("QuestionAnswer.html")
@app.route("/check_database", methods = ["POST"])
def checkdatabase():
    print( request.get_json())
    name = request.get_json()['name']
    collection =  mongo.db.get_collection(name)
    collection.find
   
    return  JSONEncoder().encode(collection.find_one({'Question':"What are the underlying causes and contributing factors?"}))
    # run app in debug mode on port 5000
app.run(debug=True, port=5001, host='0.0.0.0')

# @app.route("/ask", methods= ["GET","POST"])
# def checkData():
#     if request.method == "POST":
#         data = request.form["data"]
#         print(data)
#         return render_template("QuestionAnswer.html")