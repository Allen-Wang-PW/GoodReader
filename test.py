# -*- coding: utf-8 -*-

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from gensim.summarization.summarizer import summarize

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = "Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion."

text = """
Advertisement
Supported by
By Ben Hubbard
BEIRUT, Lebanon — After two weeks of shifting stories, Saudi Arabia said Saturday that its agents strangled Jamal Khashoggi, a dissident journalist, during a fistfight inside the Saudi Consulate in Istanbul and that 18 men had been arrested in the case.
Those arrested included 15 men who were sent to confront Mr. Khashoggi, plus one driver and two consular staff members, a Saudi official said.
Saudi state media reported that Saud al-Qahtani, a close aide to the crown prince, had been dismissed, along with Maj. Gen. Ahmed al-Assiri, the deputy director of Saudi intelligence, and other high-ranking intelligence officials. The Saudi official said General Assiri had organized the operation and that Mr. Qahtani had known about it and contributed to an aggressive environment that allowed it to escalate.
President Trump on Friday night said that Saudi Arabia’s statements were credible and that, along with its announcement of arrests, amounted to “good first steps.”
Mr. Trump, who has built strong ties with the Saudi crown prince, Mohammed bin Salman, said that he would consider “some form of sanction” in response, but that he “would prefer we don’t use as retribution” the cancellation of $110 billion worth of arms sales to the Saudis.
But Representative Adam Schiff of California was not buying the Saudi explanation. Mr. Schiff, the senior Democrat on the House Intelligence Committee, said in an interview Friday night that “if Khashoggi was fighting inside the Saudi consulate in Istanbul, he was fighting for his life with people sent to capture or kill him.”
Mr. Schiff, who said he had received a detailed, classified briefing earlier in the day on what American spy services believe were the circumstances, said that the Saudi version “was not credible.” He said he could not disclose what the intelligence agency briefers told him.
Since Mr. Khashoggi disappeared after entering the consulate on Oct. 2, Saudi Arabia has offered various, changing explanations for his disappearance, all of which seemed to distance top leadership from responsibility.
The Saudis initially claimed that Mr. Khashoggi had left the consulate alive and professed to be worried about his fate, later hinting that the killing might have been the act of rogue agents.
But international outrage mounted as Turkish officials leaked lurid details from their own investigation suggesting that he was murdered inside the consulate and dismembered by a team of Saudi agents who flew in specifically to kill him.
The case has battered the international reputation of the kingdom and the 33-year-old Prince Mohammed, who has sought to sell himself to the world as a young reformer shaking off his country’s conservative past. But suspicions that such a complicated foreign operation could not have been launched without at least his tacit approval have driven away many of his staunchest foreign supporters.
For the first time on Saturday, a Saudi official familiar with the government’s handling of the situation put forward the kingdom’s narrative of the events that led to Mr. Khashoggi’s death.
The kingdom had a general order to return dissidents living abroad, said the official, who spoke on condition of anonymity because the investigation was continuing. When the consulate in Istanbul reported that Mr. Khashoggi would be coming on Oct. 2 to pick up a document needed for his coming marriage, General Assiri dispatched a 15-man team to confront him.
The team included Maher Abdulaziz Mutrib, a security officer identified by The New York Times this week as a frequent member of the crown prince’s security detail during foreign trips, the official said. Mr. Mutrib had been chosen because he had worked with Mr. Khashoggi a decade ago in the Saudi Embassy in London and knew him personally.
But the order to return Mr. Khashoggi to the kingdom was misinterpreted as it made its way down the chain of command, the Saudi official said, and a confrontation ensued when Mr. Khashoggi saw the men. He tried to flee, the men stopped him, punches were thrown, Mr. Khashoggi screamed and one of the men put him in a chokehold, strangling him to death, the official said.
“The interaction in the room didn’t last very long at all,” the official said.
The team then gave the body to a local collaborator to dispose of, meaning that the Saudis do not know where it ended up, the official said.
All 15 members of the team had been identified by name by the Turks, and Turkish newspapers had published their photographs. The New York Times established that most of them were employed by the Saudi military or security services and that at least four had traveled with the crown prince as part of his security detail.
The Turks had said the body had been disassembled with a bone saw by an autopsy specialist flown in specifically for that purpose and probably carried out of the consulate in large suitcases.
Turkish investigators were searching a park and a forest this week for traces of Mr. Khashoggi’s remains but did not announce their findings.
The reports of Mr. Khashoggi’s killing have shaken members of the Saudi royal family, many of whom were angry about Crown Prince Mohammed’s swift rise over the past three years. Some wondered if the scandal could lead his father, King Salman, to replace him with another prince not tarnished by the case.
But instead, the king named Crown Prince Mohammed as head of a committee to restructure the kingdom’s intelligence agency.
People with knowledge of the Saudi plans had told The Times on Thursday that the kingdom was planning to blame the operation on General Assiri, the deputy intelligence director. The people said the kingdom would portray the operation as carried out by rogue actors who did not have orders from the top and who had set out to interrogate and kidnap Mr. Khashoggi but ended up killing him, perhaps accidentally.
The dismissal of Mr. Qahtani, considered a close aide to Crown Prince Mohammed, stood out because he is plays no public role in security or intelligence. He is in charge of media and communications for the crown prince, and often leads aggressive online attacks against critics of the kingdom.
The Saudi official said Mr. Qahtani had been fired because he had known about the operation and had contributed to an aggressive environment that allowed it to turn violent. While dismissed as an adviser to the royal court, Mr. Qahtani kept his job as head of a cybersecurity organization.
Mr. Khashoggi, 60, was one of Saudi Arabia’s best known personalities, a journalist who had interviewed Osama bin Laden in Afghanistan years before he founded Al Qaeda. He later served as an adviser to and unofficial spokesman for the Saudi royal family.
But his relationship with the kingdom changed during the rise of Crown Prince Mohammed, who has announced broad social and economic reforms but has also gone after critics and cut down many of his fellow royals.
After many of his friends and colleagues were jailed last year, Mr. Khashoggi settled into self-exile in the Washington area and became a columnist for The Washington Post, a position he used to criticize the crown prince’s increasing authoritarianism.
When Mr. Khashoggi did not emerge from the Saudi Consulate in Istanbul after several hours on Oct. 2, his fiancée, Hatice Cengiz, began calling Turkish officials to tell them that he was missing.
Saudi Arabia chose to make its announcement in the middle of the night over a weekend in Riyadh and Istanbul. A Turkish official said it was too soon for Ankara to comment, but reaction on social media and elsewhere was dismissive.
Samantha Power, a former ambassador to the United Nations under President Barack Obama, said on Twitter that the Saudis were “shifting from bald-face lies (‘#Khashoggi left consulate’) to faux condemnation (of a ‘rogue operation’) to claiming the fox will credibly investigate what he did to the hen.”
At the United Nations, Secretary General António Guterres cited “the need for a prompt, thorough and transparent investigation into the circumstances of Mr. Khashoggi’s death and full accountability for those responsible.”
But Ali Shihabi, the founder of the Arabia Foundation in Washington and a prominent advocate for the kingdom’s policies, defended the belated statement, arguing that an initial cover-up that hid the truth from the royal court explained the delay.
“Part of the reason for firing so many top intelligence officials was due to the cover-up and slowness in conveying the full details of what happened to the leadership,” he wrote on Twitter. “This tragic fiasco was a huge shock to the Saudi leadership and a combination of confusion, lack of experience in such crisis management and a cover-up by the intelligence bureaucracy contributed to the initial Saudi response.”
Jon B. Alterman, director of the Middle East Program at the Center for Strategic and International Studies, said the Saudis will have to provide more information — which may or may not comport with the intelligence that Turkey and the United States have gathered over the past two weeks.
“This has to be the beginning of a multiday effort that is long overdue,” Mr. Alterman said.
The Saudi statement, for example, offered no explanation for why Mr. Khashoggi would enter into an altercation with multiple foes in territory he knew to be dangerous. Mr. Khashoggi was regarded as low key and even-tempered by those who knew him. He felt nervous enough about his safety entering the consulate that he told his fiancée to wait outside with instructions to call the Turkish authorities if he did not come out.
Whether the United States or Turkey is willing to dispute or contradict the Saudi explanation is far from clear. The Saudi narrative seemed to dodge the question of whether the men had been acting at the direction of top officials, as well as the question of where Mr. Khashoggi’s body was.
The Trump administration has spent weeks trying to salvage Saudi Arabia’s role in its strategy to isolate Iran, which will be punctuated by the Nov. 5 reimposition of onerous sanctions lifted under the 2015 Iran nuclear accord.
The Turkish government has said it has recordings that suggest the Saudis ambushed Mr. Khashoggi in the consulate and dismembered him. But Turkey, in the midst of a difficult economic period that could benefit from Saudi investment, may never reveal those recordings.
Elliott Abrams, a former top diplomat in Republican administrations, said that the Saudi acknowledgment was an important first step but that many questions remain unanswered.
“Where is Jamal Khashoggi’s body, for one?” Mr. Abrams asked. “And it’s just hard to believe these people acted without instructions.”
Mr. Abrams also dismissed the core of the Saudi explanation that Mr. Khashoggi had decided to put up a fight.
“He’s in the consulate surrounded by a crowd of men and he starts a fight?” Mr. Abrams asked. “It’s just not credible.”
David D. Kirkpatrick contributed reporting from London, Eric Schmitt and Gardiner Harris from Washington, Emily Cochrane from Glendale, Ariz., and Rick Gladstone from New York.
video
Advertisement

"""
document = types.Document(
    content=str(text),
    type=enums.Document.Type.PLAIN_TEXT)

print summarize(text)



# Detects the sentiment of the text
# sentiment = client.analyze_sentiment(document=document).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))



entities = client.analyze_entities(document).entities

print type(entities)

# entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
				'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

for entity in entities:
	print('=' * 20)
	print(u'{:<16}: {}'.format('name', entity.name))
	print entity.type
	print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
	print(u'{:<16}: {}'.format('metadata', entity.metadata))
	print(u'{:<16}: {}'.format('salience', entity.salience))
	print(u'{:<16}: {}'.format('wikipedia_url',
		entity.metadata.get('wikipedia_url', '-')))

# categories = client.classify_text(document).categories

# for category in categories:
#     print(u'=' * 20)
#     print(u'{:<16}: {}'.format('name', category.name))
#     # print type(category.name)
#     print str(category.name)
#     print(u'{:<16}: {}'.format('confidence', category.confidence))