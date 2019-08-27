import channels_module

# channels_to_post = (channels_module.noisy_tests)

channels_to_post = [i[0] for i in channels_module.channels_to_post.values() for j in range(i[1])]