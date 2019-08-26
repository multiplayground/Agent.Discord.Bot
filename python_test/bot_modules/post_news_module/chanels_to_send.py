import channels_module

# channels_to_post = (channels_module.discussion_busines,channels_module.discussion_disc_bot
#                         ,channels_module.discussion_gen_chat,channels_module.discussion_mlp_core
#                         ,channels_module.discussion_web_site)

channels_to_post = [i[0] for i in channels_module.channels_to_post.values() for j in range(i[1])]