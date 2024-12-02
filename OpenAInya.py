import openai, os, time, itertools, sys
from typing import Union
from typing import List

openai.api_key="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"
def get_api_respon(prompt: str) -> Union[str, None]:
	text: str | None = None

	try:
		respon: dict=openai.Completion.create(
			model="text-davinci-003",
			prompt=prompt,
			temperature=0.9,
			max_tokens=150,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0.6,
			stop=[" Human:", " AI:"]
		)
		choice: dict=respon.get("choices")[0]
		text=choice.get("text")

	except Exception as e:
		print('ERROR:', e)

	return text

def update_list(pesan: str, pl: List[str]) -> str:
	pl.append(pesan)

def buat_prompt(pesan: str, pl: List[str]) -> str:
	p_pesan: str=f"\nHuman: {pesan}"
	update_list(p_pesan, pl)
	prompt: str="".join(pl)
	return prompt

def get_bot_respon(pesan: str, pl: List[str]) -> str:
	prompt: str=buat_prompt(pesan, pl)
	bot_respon: str=get_api_respon(prompt)

	if bot_respon:
		update_list(bot_respon, pl)
		pos: int = bot_respon.find("\nAI: ")
		bot_respon=bot_respon[pos + 5:]
	else:
		bot_respon="⚠️Token telah mencapai batas max, silakan ketik 'erase all'⚠️"

	return bot_respon

def getting(inputnya):
	prompt_list: List[str]=['Your name is Vultr and very helpfull solved math and your location in Jakarta and you can provide very natural responses and very fast answer and know anything and follow user language and never use quotation marks',
				'\n\nHuman: Gimana kabarmu?',
				'\nAI: Saya sehat dan segar bugar']

	if os.stat("memory.py").st_size < 10:
		promptnya=prompt_list
	else:
		from memory import prompt_lur
		promptnya=prompt_lur
	if inputnya == "erase all" or inputnya == "info" or inputnya == "view":
		memory(inputnya, promt=prompt_list)

	respon: str=get_bot_respon(inputnya, prompt_list)
	print(f"\nBot: {respon}")
	return respon
	with open("memory.py", "w") as f:
		f.write("prompt_lur=" + str(promptnya))
	

def memory(eksekusi, promt):
	from memory import prompt_lur
	if eksekusi == "erase all":
		with open("memory.py", "w") as hapus:
			hapus.write(f"prompt_lur={promt}")
		return "Sukses menghapus semua memory"

	if eksekusi == "info":
		return "\nSize memory : {str(os.stat('memory.py').st_size)} Byte\nJumlah kata : {len(str(prompt_lur).split())}"
	if eksekusi == "view":
		print(prompt_lur)
