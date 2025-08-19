import matplotlib.pyplot as plt



AIA_MLP_ViT = [0.222, 0.109, 0.082, 0.065, 0.053]

AIA_KAN_ViT = [0.271, 0.138, 0.098, 0.079, 0.056]

# AIA_MLP = [0.9931640625, 0.4997702205882353, 0.326763117313385, 0.24805501302083333, 0.20924479166666665]
# AIA_KAN = [0.9951171875, 0.5019818474264706, 0.33346693165162034, 0.26481911256982416, 0.4650079884285144]


plt.plot(AIA_KAN_ViT, label='AIA_CL_ViT_KAN')
plt.plot(AIA_MLP_ViT, label='AIA_CL_ViT_MLP')
plt.ylabel('Average Incremental Accuracy (AIA)')
plt.xlabel('No of Tasks')
plt.legend()
file_name = 'AIA_KAN_vs_MLP.png'
plt.savefig(file_name)
plt.show()



# plt.plot(AIA_KAN, label='AIA_KAN')
# plt.plot(AIA_MLP, label='AIA_MLP')
# plt.ylabel('Average Incremental Accuracy (AIA)')
# plt.xlabel('No of Tasks')
# plt.legend()
# file_name = 'AIA_KAN_vs_MLP.png'
# plt.savefig(file_name)
# plt.show()