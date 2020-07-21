def eh_magico(matriz):
    # verifica se eh quadrada
    num_linhas = len(matriz)
    for linha in matriz:
        if len(linha) != num_linhas:
            return False

    # pegou o valor de referencia
    soma_ref = sum(matriz[0])

    # verificou a soma das linhas
    for linha in matriz:
        if sum(linha) != soma_ref:
            return False

    # verifica a soma das colunas
    for col in range(len(matriz)):
        soma_coluna = 0
        for lin in range(len(matriz)):
            soma_coluna += matriz[lin][col]

        if soma_coluna != soma_ref:
            return False

    # verifica a soma da diagonal principal
    soma_diag_principal = 0
    for i in range(len(matriz)):
        soma_diag_principal += matriz[i][i]
    if soma_diag_principal != soma_ref:
        return False

    # verifica a soma da diagonal secundaria
    lin = len(matriz) - 1
    col = 0
    soma_diag_secundaria = 0
    for i in range(len(matriz)):
        soma_diag_secundaria += matriz[lin][col]
        lin -= 1
        col += 1
    if soma_diag_secundaria != soma_ref:
        return False
    
    # se a execucao chegou ateh aqui, eh pq todas as
    # condicoes do quadrado magico foram satisfeitas
    # soh resta retornar True com a certeza:
    # a matriz eh sim um quadrado magico
    return True

mat = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2],
]

quad10 = [
    [68, 65, 96, 93, 4, 1, 32, 29, 60, 57],
    [66, 67, 94, 95, 2, 3, 30, 31, 58, 59],
    [92, 89, 20, 17, 28, 25, 56, 53, 64, 61],
    [90, 91, 18, 19, 26, 27, 54, 55, 62, 63],
    [16, 13, 24, 21, 49, 52, 80, 77, 88, 85],
    [14, 15, 22, 23, 50, 51, 78, 79, 86, 87],
    [37, 40, 45, 48, 76, 73, 81, 84, 9, 12],
    [38, 39, 46, 47, 74, 75, 82, 83, 10, 11],
    [41, 44, 69, 72, 97, 100, 5, 8, 33, 36],
    [43, 42, 71, 70, 99, 98, 7, 6, 35, 34],
]

quad30 = [
    [488, 485, 556, 553, 624, 621, 692, 689, 760, 757, 828, 825, 896, 893, 4, 1, 72, 69, 140, 137, 208, 205, 276, 273, 344, 341, 412, 409, 480, 477],
    [486, 487, 554, 555, 622, 623, 690, 691, 758, 759, 826, 827, 894, 895, 2, 3, 70, 71, 138, 139, 206, 207, 274, 275, 342, 343, 410, 411, 478, 479],
    [552, 549, 620, 617, 688, 685, 756, 753, 824, 821, 892, 889, 60, 57, 68, 65, 136, 133, 204, 201, 272, 269, 340, 337, 408, 405, 476, 473, 484, 481],
    [550, 551, 618, 619, 686, 687, 754, 755, 822, 823, 890, 891, 58, 59, 66, 67, 134, 135, 202, 203, 270, 271, 338, 339, 406, 407, 474, 475, 482, 483],
    [616, 613, 684, 681, 752, 749, 820, 817, 888, 885, 56, 53, 64, 61, 132, 129, 200, 197, 268, 265, 336, 333, 404, 401, 472, 469, 540, 537, 548, 545],
    [614, 615, 682, 683, 750, 751, 818, 819, 886, 887, 54, 55, 62, 63, 130, 131, 198, 199, 266, 267, 334, 335, 402, 403, 470, 471, 538, 539, 546, 547],
    [680, 677, 748, 745, 816, 813, 884, 881, 52, 49, 120, 117, 128, 125, 196, 193, 264, 261, 332, 329, 400, 397, 468, 465, 536, 533, 544, 541, 612, 609],
    [678, 679, 746, 747, 814, 815, 882, 883, 50, 51, 118, 119, 126, 127, 194, 195, 262, 263, 330, 331, 398, 399, 466, 467, 534, 535, 542, 543, 610, 611],
    [744, 741, 812, 809, 880, 877, 48, 45, 116, 113, 124, 121, 192, 189, 260, 257, 328, 325, 396, 393, 464, 461, 532, 529, 600, 597, 608, 605, 676, 673],
    [742, 743, 810, 811, 878, 879, 46, 47, 114, 115, 122, 123, 190, 191, 258, 259, 326, 327, 394, 395, 462, 463, 530, 531, 598, 599, 606, 607, 674, 675],
    [808, 805, 876, 873, 44, 41, 112, 109, 180, 177, 188, 185, 256, 253, 324, 321, 392, 389, 460, 457, 528, 525, 596, 593, 604, 601, 672, 669, 740, 737],
    [806, 807, 874, 875, 42, 43, 110, 111, 178, 179, 186, 187, 254, 255, 322, 323, 390, 391, 458, 459, 526, 527, 594, 595, 602, 603, 670, 671, 738, 739],
    [872, 869, 40, 37, 108, 105, 176, 173, 184, 181, 252, 249, 320, 317, 388, 385, 456, 453, 524, 521, 592, 589, 660, 657, 668, 665, 736, 733, 804, 801],
    [870, 871, 38, 39, 106, 107, 174, 175, 182, 183, 250, 251, 318, 319, 386, 387, 454, 455, 522, 523, 590, 591, 658, 659, 666, 667, 734, 735, 802, 803],
    [36, 33, 104, 101, 172, 169, 240, 237, 248, 245, 316, 313, 384, 381, 449, 452, 520, 517, 588, 585, 656, 653, 664, 661, 732, 729, 800, 797, 868, 865],
    [34, 35, 102, 103, 170, 171, 238, 239, 246, 247, 314, 315, 382, 383, 450, 451, 518, 519, 586, 587, 654, 655, 662, 663, 730, 731, 798, 799, 866, 867],
    [97, 100, 165, 168, 233, 236, 241, 244, 309, 312, 377, 380, 445, 448, 516, 513, 581, 584, 649, 652, 717, 720, 725, 728, 793, 796, 861, 864, 29, 32],
    [98, 99, 166, 167, 234, 235, 242, 243, 310, 311, 378, 379, 446, 447, 514, 515, 582, 583, 650, 651, 718, 719, 726, 727, 794, 795, 862, 863, 30, 31],
    [161, 164, 229, 232, 297, 300, 305, 308, 373, 376, 441, 444, 509, 512, 577, 580, 645, 648, 713, 716, 721, 724, 789, 792, 857, 860, 25, 28, 93, 96],
    [163, 162, 231, 230, 299, 298, 307, 306, 375, 374, 443, 442, 511, 510, 579, 578, 647, 646, 715, 714, 723, 722, 791, 790, 859, 858, 27, 26, 95, 94],
    [225, 228, 293, 296, 301, 304, 369, 372, 437, 440, 505, 508, 573, 576, 641, 644, 709, 712, 777, 780, 785, 788, 853, 856, 21, 24, 89, 92, 157, 160],
    [227, 226, 295, 294, 303, 302, 371, 370, 439, 438, 507, 506, 575, 574, 643, 642, 711, 710, 779, 778, 787, 786, 855, 854, 23, 22, 91, 90, 159, 158],
    [289, 292, 357, 360, 365, 368, 433, 436, 501, 504, 569, 572, 637, 640, 705, 708, 773, 776, 781, 784, 849, 852, 17, 20, 85, 88, 153, 156, 221, 224],
    [291, 290, 359, 358, 367, 366, 435, 434, 503, 502, 571, 570, 639, 638, 707, 706, 775, 774, 783, 782, 851, 850, 19, 18, 87, 86, 155, 154, 223, 222],
    [353, 356, 361, 364, 429, 432, 497, 500, 565, 568, 633, 636, 701, 704, 769, 772, 837, 840, 845, 848, 13, 16, 81, 84, 149, 152, 217, 220, 285, 288],
    [355, 354, 363, 362, 431, 430, 499, 498, 567, 566, 635, 634, 703, 702, 771, 770, 839, 838, 847, 846, 15, 14, 83, 82, 151, 150, 219, 218, 287, 286],
    [417, 420, 425, 428, 493, 496, 561, 564, 629, 632, 697, 700, 765, 768, 833, 836, 841, 844, 9, 12, 77, 80, 145, 148, 213, 216, 281, 284, 349, 352],
    [419, 418, 427, 426, 495, 494, 563, 562, 631, 630, 699, 698, 767, 766, 835, 834, 843, 842, 11, 10, 79, 78, 147, 146, 215, 214, 283, 282, 351, 350],
    [421, 424, 489, 492, 557, 560, 625, 628, 693, 696, 761, 764, 829, 832, 897, 900, 5, 8, 73, 76, 141, 144, 209, 212, 277, 280, 345, 348, 413, 416],
    [423, 422, 491, 490, 559, 558, 627, 626, 695, 694, 763, 762, 831, 830, 899, 898, 7, 6, 75, 74, 143, 142, 211, 210, 279, 278, 347, 346, 415, 414],
]

print("mat =", eh_magico(mat))
print("quad10 =", eh_magico(quad10))
print("quad30 =", eh_magico(quad30))
