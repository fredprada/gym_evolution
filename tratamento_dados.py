# class TratarDados:
#     def __init__(self, tabela_para_salvar):
#         self.tabela_para_salvar = tabela_para_salvar


#     def func_add_row(date_of_the_game, 
#                     time_played, 
#                     pai, 
#                     played_alone, 
#                     time_of_the_game, 
#                     enthusiasm_before_playing, 
#                     rating, 
#                     listened_to_music, 
#                     rest_time, 
#                     feeling_before_game, 
#                     calorias):
#         global list_to_add
#         list_to_add=[]
#         dict_dia = {}
#         dict_dia['jogador'] = player
#         dict_dia['dia'] = date_of_the_game.strftime("%Y-%m-%d")
#         dict_dia['hora_do_jogo'] = time_of_the_game.strftime("%H:%M")
#         dict_dia['tempo_de_descanso'] = str(rest_time)
#         dict_dia['jogou_sozinho'] = str(played_alone)
#         dict_dia['ouviu_musica'] = str(listened_to_music)
#         dict_dia['nota'] = str(rating)
#         dict_dia['pai'] = str(pai)
#         dict_dia['calorias'] = str(calorias)
#         dict_dia['tempo_jogado'] = str(time_played)
#         dict_dia['animo_pra_jogar'] = str(enthusiasm_before_playing)
#         dict_dia['sentimento_do_dia'] = str(feeling_before_game)
#         list_to_add.append(dict_dia)
#         return list(list_to_add)