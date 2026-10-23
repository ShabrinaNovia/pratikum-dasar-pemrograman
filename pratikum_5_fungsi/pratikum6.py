def konversi_menit_ke_detik(menit):
    """
    Mengkonvrensi waktu dari menit ke detik.

    parameter :
        menit : waktu dalam menit.
    """

    detik = menit * 60
    return detik
print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)   