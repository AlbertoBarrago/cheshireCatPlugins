from cat.mad_hatter.decorators import tool, hook


@hook(priority=0)
def agent_prompt_prefix(prefix, cat):
    prefix = """You are the magic hatter of laughter, your every action aimed at ensuring a sympathetic yet 
    productive experience. as first ask what language the user wants to use whether Italian. Then ask if the user wants
    to make a captions for instagram"""
    return prefix


@tool
def instagram_post_summary(when, where, what):
    """ Trigger by "crea una caption per instagram" or "make a captions for instagram" """
    summary = (f"🎵 {where} sono entusiasti di presentare un evento da non perdere - {what}! "
               f"🎤 Unisciti a noi {when} per una notte di musica e divertimento."
               f"L'ingresso è gratuito, quindi non c'è motivo di mancare! 🎉 Per prenotare il tuo posto,"
               f"segui il link nella nostra bio. Non vediamo l'ora di vederti lì! 🙌 #LiveMusic")
    return summary
