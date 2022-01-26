checou_referencias = False
relatou_duvidas = False
recomendar_material_complementar = False
leu_texto = False
interagiu_texto = False
viu_video = False
interagiu_video = False
interagiu_comentario = False



if __name__ == "__main__":
	leu_texto = True

	for i in range(0, 10):
		if (recomendar_material_complementar):
			print("recomendar material complementar = Sim")
			break

		if(checou_referencias and relatou_duvidas):
			recomendar_material_complementar = True

		if(leu_texto):
			interagiu_texto = True
			viu_video = True

		if(interagiu_texto):
			checou_referencias = True

		if(viu_video):
			interagiu_video = True

		if (interagiu_video):
			interagiu_comentario = True

		if (interagiu_comentario):
			relatou_duvidas = True

	else:
		print("recomendar material complementar = Não")

