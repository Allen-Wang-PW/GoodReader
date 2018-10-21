# -*- coding: utf-8 -*-

import NLP as nlp

if __name__ == "__main__":
	text = """
	 Journalist Jamal Khashoggi died after a fight in the Saudi consulate in Istanbul, the country's state TV reported quoting an initial probe.

It said deputy intelligence chief Ahmad al-Assiri and Saud al-Qahtani, senior aide to Crown Prince Mohammed Bin Salman, were dismissed over the affair.

US President Donald Trump said what happened was "unacceptable" but Saudi Arabia was a "great ally".

This is the first time the kingdom has admitted Mr Khashoggi has died.

Speaking at a round table event, President Trump said the arrests were an important "first step". He praised the kingdom for acting quickly, and while he said sanctions were an option against the country, he spoke of the possible effect such moves would have on the US economy.

Asked if he found Saudi Arabia's version of events credible, he replied, "I do."

Saudi King Salman has also reportedly ordered the formation of a ministerial committee, headed by Crown Prince Mohammed, to restructure the intelligence services.

The journalist was last seen entering the Saudi consulate in Istanbul on 2 October, to pick up paperwork that would allow him to marry his fiancée Hatice Cengiz.

Reports on Saudi state media followed shortly after King Salman spoke on the phone to Turkey's President Recep Tayyip Erdogan about the case.

The Jamal Khashoggi story so far
Who's who in alleged Saudi 'hit squad'
Khashoggi suspect had 'cyber spy' training
Saudi Arabia reportedly acted on information provided by Turkish authorities as part of its inquiry, investigating a number of suspects.

"""
	processor = nlp.NLP(text)
	print processor.getInsight()
	pass