import streamlit as st
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
import altair as alt
#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation
st.set_page_config(page_title="Bytes and Bombs", page_icon="🚨", layout="centered")
#pip install streamlit to instsall streamlit.io
def introduction_page():
    st.markdown("<h2 style='color: #990000;'>Bytes and Bombs: The Internet and Cyber-Terrorism</h2>",
                unsafe_allow_html=True)
    st.sidebar.success("")

    image_url = "https://media.giphy.com/media/oYQ9HRm5Mo7VXeMNVR/giphy.gif"
    st.image(image_url, caption='Image from > https://giphy.com/gifs/glitch-error-basic-oYQ9HRm5Mo7VXeMNVR',
             use_column_width=True)

    st.markdown("<h2 style='color: #990000;'>Introduction</h2>", unsafe_allow_html=True)


    st.write(
        "Although terrorism can have various definitions, it is consistently associated with a negative connotation. "
        "The Nacos Definition states: 'Terrorism is political violence or the threat of violence by groups or "
        "individuals who deliberately target noncombatants to influence the behavior and actions of targeted publics "
        "and governments.' ")
    st.write(
        "I urge everyone to critically examine this definition and identify its shortcomings. However, "
        "it is important to note that it is genuinely impossible to formulate or enforce international law without a "
        "standardized definition. In many cases, the lack of a uniform definition leads to loopholes due to the "
        "differing interpretations of each country.")
    st.write(
        'According to Brian Michael Jenkins, in his work "The Study of Terrorism: Definitional Problems," the term '
        '"terrorism" is described as "a fad word used promiscuously and often applied to a variety of acts of '
        'violence which are not strictly limited.... terrorism is what the bad guys do" (Jenkins), does an excellent '
        'job of highlighting the issue of definitional challenges and the varying definitions that can come with an '
        'unspecified and non-meticulous reality of the term.')
    st.write(
        'An example of the failure of getting the definition “right” would be the US State Department characterizes '
        'it as "politically motivated violence perpetrated against noncombatant targets by subnational groups or '
        'clandestine agents, usually intended to influence an audience." While this definition serves as an attempt '
        'to capture what they believe to be terrorism, it is full of contradictions and complexities.')
    st.write(
        'One inherent challenge lies in the subjectivity of the term "politically motivated violence." What '
        'constitutes political motivation can vary widely, subject to individual or group perspectives. Additionally, '
        'the specification of "noncombatant targets" adds another layer of complexity. The distinction between '
        'combatants and noncombatants is not always clear, particularly in modern conflicts where the lines between '
        'these categories can blur. This ambiguity may lead to contradictions in the application of the definition. ')
    st.write(
        'While this describes terrorism on a broader range, like these many different definitions, cyber-terrorism '
        'too has not universally accepted definition. According to the text entitled “Understanding Cyber Terrorism '
        'from Motivational Perspectives”, by Yunos, Z, and S Sulaman, for an attack to be labeled as cyber terrorism, '
        'it must have a motivational component, result in death and/or large-scale destruction, and be politically '
        'motivated. The aim is to cause grave harm, severe economic damage, or extreme financial harm. Including this '
        'it is stated that there are three key elements must be satisfied to constitute cyber terrorism, '
        'including politically motivated cyber-attacks leading to death or bodily injury, cyber attacks causing fear '
        'and physical harm, and serious attacks targeting critical information infrastructures such as financial, '
        'energy, transportation, and government operations. ')

def loading_animation():
    st.title("Bytes and Bombs")
    st.write("This project delves into the challenges of defining terrorism and the evolution of cyber-threats, "
             "highlighting the complex nature of radicalization and counter terrorism efforts. "
             )
    user_name = "Ayanna Bailey- Arias"
    st.write(f"{user_name}")

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Loading... {i + 1}%")
        time.sleep(0.1)

    progress_bar.empty()
    status_text.empty()

    # Clear the entire page after animation
    st.empty()

    # Display the introduction page
    introduction_page()

def main():
    loading_animation()

if __name__ == "__main__":
    main()

st.markdown("<h2 style='color: #990000;'>Radicalization</h2>", unsafe_allow_html=True)

article_intro = """
The article entitled “Rethinking Online Radicalization” by Joe Whittaker does an excellent job at challenging 
the understanding of online radicalization by arguing against the separation between the “online” and “offline” realms. 
The article suggests both domains are inseparable, and we should understand the ontological nature of it and by doing 
this adopting a broader range of factors beyond online communication technologies when studying radicalization.
"""

article_main = """
The article refers to various models and theories proposed by scholars to explain the dynamics of online radicalization, 
emphasizing the potential for individuals to be exposed to extremist propaganda, engage in deviant behaviors, and form 
online communities that facilitate radicalization. When trying to theorize the process of online and offline dynamics, 
the article acknowledges the ambiguity of the term online radicalization and suggests that scholars should move beyond 
the narrow focus on online radicalization. It recommends considering the wider information environment while avoiding 
theories that exclusively explain how online radicalization works and advocates for holistic theories that consider 
individuals' predispositions, stressors, engagement with their environment, and systemic factors.
"""

police_text = """
In correlation to this, the text by the International Association of Chiefs Police, entitled 
“Online Radicalization to Violent Extremism,” briefly touches on the topic highlighting the process by which individuals 
are exposed to extremist ideologies and gradually move from mainstream beliefs toward more extreme views. Online media, 
particularly social networks like Facebook, Twitter, and YouTube, play a significant role in this process. The text 
emphasizes that the factors influencing radicalization vary from person to person, and the process itself can be dynamic, 
with individuals moving back and forth between stages. This also leads into different perspectives.
"""

# Displaying the content using Streamlit
st.write(article_intro)
st.write(article_main)
st.write(police_text)

st.markdown("Firstly, the social perspective and the induvial focus; The concept of radicalization usually emphasizes "
            "the psychological factors, and the effect online platforms and social media have on the induvial "
            "constantly this rhetoric of construed violent beliefs. Group dynamics also play an important in this "
            "first perspective because not only can the group influence tend to pull individuals towards extremist "
            "ideologies, but the engagement also associated with the mind of interaction and sense of belonging "
            "become an intense pull factor towards those ideas")
st.write("The psychological perspective such as individual vulnerabilities due to grievances and confirmation bias, "
         "wherein individuals seek information aligning with their existing beliefs, contributes to the reinforcement "
         "of radical ideologies act as factors for this perspective however, the line can become misconstrued for "
         "example, the horrific crimes Anders Breivik committed, the question of mental health became a key topic in "
         "his trail, although sentenced to 21 years, the question still remains of mental health as strategic factor "
         "for mitigated legal consequences or for public sympathy.")
st.write("Another less widely looked at perspective is the political perspective where an individual's ideologies are "
         "fueled by key factors including but not limited, to their socio-political and economic conditions marked by "
         "discrimination, inequality, and the use of propaganda. ")

# Import necessary libraries

st.markdown("<h2 style='color: #990000;'>The Internet and Cyber-Terrorism</h2>", unsafe_allow_html=True)
st.write("Not limited to real world actualities of radicalization, within the cyber sphere, terrorist aim to use "
         "cyber capabilities to further their ideological or political goals. This can include hacking into websites, "
         "launching distributed denial-of-service (DDoS) attacks and spreading propaganda. Cyber terrorists may "
         "target critical infrastructure, government systems, financial institutions, or any entity that does not "
         "align with their ideological or political objectives with the goal to cause disruption, fear, or economic "
         "damage. ")
st.write('The Security Brief, New Zealand article entitled "A brief history of cyber-threats — from 2000 to 2020" by '
         'Nick Forrester, provides a historical perspective on cyber-threats, "A brief history of cyber-threats — '
         'from 2000 to 2020" details the events and the increase in cyberattacks in different countries starting all '
         'the way from the early 2000’s entitling it the “Worm Era” he details the wave of prolific “worms” costing '
         'in over 100 billion dollars in damages and remediation costs to the information security industry  The '
         'notorious ILOVEYOU worm, unleashed in 2000, targeted Microsoft Outlook users, infecting 10% of '
         'internet-connected hosts within hours and causing up to 15 billion dollars in damages. Subsequent worms '
         'like CodeRed, Nimda, and Blaster exploited vulnerabilities in operating systems and network infrastructure '
         'as seen in the chart below. ')

# Data
data = {
    "Worm": ["CodeRed", "Code Red II", "Nimda", "SQL Slammer", "Blaster", "Welchia", "Sobig.F", "Sober", "Bagle", "MyDoom", "Netsky", "Sasser"],
    "Month": ["July 2001", "August 2001", "September 2001", "January 2003", "August 2003", "August 2003", "August 2003", "October 2003", "January 2004", "January 2004", "February 2004", "April 2004"]
}

df = pd.DataFrame(data)

# Chart
st.title("Worms of the Early 2000s")
chart = alt.Chart(df).mark_bar().encode(
    y=alt.Y("Worm:N", title=None, sort='-x'),
    x=alt.X("Month:N", title="Month of Emergence"),
    color=alt.Color("Month:N", legend=None)
).properties(width=600, height=300)

st.altair_chart(chart, use_container_width=True)

st.write("Moving on the 2005-2013 era which was entitled the “Monetisation Era”, With the use of malvertising, spam, "
         "botnets, and trojans they terrorists were able to capitalize off this for money and profit instead of for "
         "notoriety. Spam, was initially used for spreading worms and eventually evolved into a monetized tool for "
         "online scams, particularly through coordinated campaigns like pharmacy spam. One notable development was "
         "the Storm botnet, renowned as the 'most powerful supercomputer,' designed for stealth and profit. The "
         "botnet employed advanced techniques, such as a distributed peer-to-peer model, fast-flux DNS, "
         "and polymorphism, setting a standard for future botnets. Additionally, the monetization era saw the rise of "
         "the Zeus/Zbot banking trojan, transforming from a banking trojan to a full-fledged crimeware kit. The "
         "leaked Zeus source code in 2011 spawned several variants, contributing to the era of crimeware-as-a-service "
         "to be capitalized off of.")
st.write("Lastly, in the Ransomware Era from 2013-2020, with estimated damages in the trillions of dollars, "
         "ransomware, most notably CryptoLocker  exploits vulnerabilities in IT defenses, utilizing encryption and "
         "cryptocurrency and double extortion. Cyber-criminals not only encrypt and steal data but also threaten to "
         "publish it unless a ransom is paid. No individual or industry is immune, and no single technology is "
         "foolproof against ransomware attacks.")
st.write("Below shows the region in which different crimes have been committed the most.")

# Sample data (replace this with your actual data)
data = {
    'Region': ['Asia', 'Europe', 'North America', 'Middle East and Africa', 'Latin America'],
    'Server Access': [20, 26, 30, 18, 29],
    'Ransomware': [11, 12, 30, 12, 21],
    'Data Theft': [10, 10, 9, 14, 21],
}

# Create a stacked bar chart
fig = px.bar(
    data,
    x='Region',
    y=['Server Access', 'Ransomware', 'Data Theft'],
    title='Distribution of Cyber Attack Types by Region (2021)',
    labels={'value': 'Percentage'},
    height=500,
)

# Update layout for better visualization
fig.update_layout(barmode='stack', legend=dict(title_text='Attack Type'))

# Display the chart using Streamlit
st.plotly_chart(fig)

st.write("Additionally, some other cyber-attacks listed by New Jersey Gov. Including android malware that purposely "
         "targets android mobile devices mobile devices that causes a range of attacks from device disablement to "
         "data theft. Similarly, it is important to not iOS devices are not immune to malware as iOS devices "
         "including the macOS are subject to this threat. \nPayment processing systems are also targets for "
         "cybercriminals seeking to steal credit and debit card data.")
# Import necessary libraries

st.markdown("<h2 style='color: #990000;'>Deradicalization and Counter Terrorism </h2>",
            unsafe_allow_html=True)
st.write("In an interview with Richard A. Clarke, a former senior White House advisor, the discussion revolves around "
         "the risks of cyber war and cyber terrorism and ways to address them. Clarke emphasizes that while "
         "cyber-attacks with limited objectives have occurred, a full-scale cyber war is yet to happen. He believes "
         "that U.S. leaders understand the threat but haven't taken sufficient action, suggesting that a large-scale "
         "cyber-attack may be necessary to alert the government causing legislative action. ")
st.write('According to Koehler, D, “Understanding Deradicalization” book, in the introduction in chapter 1, '
         'deradicalization is defined as a process of individual or collective cognitive change from criminal, '
         'radical, or extremist identities to a non-criminal or moderate psychological state. It involves turning '
         'away from a position of endorsing and using violence towards abstinence from violent means and/or '
         'attitudes. The process of deradicalization is differentiated from "disengagement," which only denotes a '
         'behavioral role change from offending to non-offending, The text also acknowledges the lack of conceptual '
         'clarity in the emerging topic on deradicalization and the variety of terms used globally to describe a '
         'similar process of moving away from violent ideologies or actions.  Additionally, in the text “The Cyber '
         'Defense Review – Countering the Cyber Threat”, it calls for the development of consensus, involving the '
         'unified effort to address the cybersecurity challenge by building consensus amongst public and private '
         'sectors. The development of public-private, cross-firm, and cross-industry liaison networks.  would be used '
         'to minimize localized thinking in threat response and enhance cooperation among firms and governments to '
         'address challenges that span different sectors. As well as this the addition of a tightly monitored '
         'information and communications network would provide rapidly declassified and anonymized threat indicators, '
         'facilitating the quick detection of emerging attacks, and enabling attribution. With these measures this '
         'will create a more team-based approach to this threat. ')
st.write('Moving away from the call to state effort counter of terrorism as countries are starting to recognize the '
         'need for specialized units to counter cyber threats, in the text “Countering Violent Extremism: A '
         'Peacebuilding Perspective”, by Goergia Holmer, the author understands the evolving nature of violent '
         'extremism, and aims for intersection between the counter violent extremism field and peacebuilding of '
         'people. While CVE primarily operates within the international and national security policymaking community '
         'for rules and regulations. peacebuilders also address the issue of violent extremism through conflict '
         'prevention efforts. The two fields increasingly intersect, although their approaches and practices may '
         'differ. With the idea of Peacebuilding contributions such as "do-no-harm" methodology, ensuring that '
         'programs do not have unintended negative consequences, building local capacity and engaging existing '
         'mechanisms, networks, and practices to contribute to Counter Violent Extremist efforts. An advocation for a '
         'more coordinated and inclusive approach that leverages the strengths of both to address the complex and '
         'evolving challenges of violent extremism. The article concludes with recommendations for holistic '
         'de-radicalization, emphasizing re-education, vocational training, financial support, and the creation of a '
         'conducive environment for reintegration. ')
# More information
#from streamlit_option_menu import option_menu
import pandas as pd  # read csv, df manipulation

# Import necessary libraries
st.markdown("<h2 style='color: #990000;'>Citations</h2>",
            unsafe_allow_html=True)
st.write("Wasburn, Philo C. J’]ournal of Political & Military Sociology 31, no. 1 (2003): 157–59. (http://www.jstor.org/stable/45294377)") #how to include a link
st.write("Yunos, Z, and S Sulaman. “Understanding Cyber Terrorism from Motivational Perspectives.” Journal of Information Warfare 16, no. 4 (2017): 1–13(https://www.jstor.org/stable/26504114.)") #how to include a link
st.write("Jacobsen, Colin, and Daniel Maier-Katkin. “Breivik’s Sanity: Terrorism, Mass Murder, and the Insanity Defense.” Human Rights Quarterly 37, no. 1 (2015): 137–5(http://www.jstor.org/stable/24518277.)") #how to include a linkst.write("Whittaker, Joe. “Rethinking Online Radicalization.” Perspectives on Terrorism 16, no. 4(2022): 27–40(https://www.jstor.org/stable/27158150)") #how to include a link
st.write(" Clarke, Richard A. “The Risk of Cyber War And Cyber Terrorism.” Journal of International Affairs 70, no. 1 (2016): 179–81.(https://www.jstor.org/stable/90012602)") #how to include a link
st.write("(https://securitybrief.co.nz/story/a-brief-history-of-cyber-threats-from-2000-to-2020)") #how to include a link
st.write("(https://www.nj.gov/njoem/mitigation/pdf/2019/mit2019_section5-16_Cyber_Attack.pdf)") #how to include a link #how to include a link
st.write("Drent, Margriet, Kees Homan, and Dick Zandee. “Case Study Cyber Security.” Civil-Military Capacities for European Security. Clingendael Institute, 2013.(http://www.jstor.org/stable/resrep05404.8.)") #how to include a link
st.write("Henry, Shawn, and Aaron F. Brantly. “Countering the Cyber Threat.” The Cyber Defense Review 3, no. 1 (2018): 47–56.(http://www.jstor.org/stable/26427375)") #how to include a link
st.write("ICT Cyber Desk. “Trends in Countering Cyber-Terrorism.” Analysis of Cyber Trends 2016, International Institute for Counter-Terrorism (ICT), 2016, pp. 17–19. JSTOR,](http://www.jstor.org/stable/resrep09459.7)")
st.write("Georgia, Holmer, “Countering Violent Extremism: A Peacebuilding Perspective”(https://www.usip.org/sites/default/files/SR336-Countering%20Violent%20Extremism-A%20Peacebuilding%20Perspective.pdf )")
st.write("Islam, Md. Didarul. “De-Radicalisation of Terrorists: Theoretical Analysis and Case Studies.” Counter Terrorist Trends and Analyses 11, no. 5 (2019): 6–12.(https://www.jstor.org/stable/26631540.)")

html_code = """
<style>
  @keyframes rotate {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #000;
  }

  .police-light {
    font-size: 4em;
    animation: rotate 1s linear infinite, stopRotate 2s linear forwards;
    color: #00f; /* Blue color for police light */
  }

  @keyframes stopRotate {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>

<div class="police-light">🚨</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
st.write("Thanks for reading!")
