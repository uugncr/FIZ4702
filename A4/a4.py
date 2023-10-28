import numpy as np
import matplotlib.pyplot as plt

# Spektrometrenin Kalibrasyon Eğrisinin Çizilmesi:
def cubic_interpolation(x, y, num_points=100):
    # X ve Y için katsayıları hesapla
    coeffs = np.polyfit(x, y, 3)
    # X aralığı için yeni değerler oluştur
    x_interpolated = np.linspace(x.min()-1, x.max()+1, num_points)
    # Y değerlerini interpolasyonu kullanarak hesapla
    y_interpolated = np.polyval(coeffs, x_interpolated)
    return x_interpolated, y_interpolated

lamda = np.array([7075, 6950, 6100, 5825, 5500, 4950, 4400, 4125])
thita_ref = 87.50
thita_deney = np.array([115.08, 115.13, 115.16, 115.33, 115.58, 116, 115.91, 116.33])

thita_deney = thita_deney - thita_ref
print("thita= ", thita_deney)
interpolated_x, interpolated_y = cubic_interpolation(thita_deney, lamda)

# Hidrojen Spektrumundan Rydberg Sabibnin Hesaplanması:
# Verilen theta değerlerine karşılık gelen lambda değerleri
theta_values = np.array([28.84, 27.92, 28.5, 29.09, 29.34])

lambda_values = np.polyval(np.polyfit(interpolated_x, interpolated_y, 3), theta_values)
print("Verilen theta değerlerine karşılık gelen lambda değerleri:", lambda_values)

# Sodyumun İnce Yapısı:
thita_ref_Na = 87
thita_deney_Na = np.array([108.5, 135.5])
thita_deney_Na = thita_deney_Na - thita_ref_Na
lambda_values_Na = np.polyval(np.polyfit(interpolated_x, interpolated_y, 3), thita_deney_Na)
print("Bulunan theta değerlerine karşılık gelen lambda değerleri:", lambda_values_Na)

# Orijinal verileri ve interpolasyon sonuçlarını çizdir
fig, ax = plt.subplots()
ax.plot(thita_deney, lamda, marker='.', label='Orijinal Veriler')
ax.plot(interpolated_x, interpolated_y, label='Kubik Interpolasyon')
ax.set_xlabel('θ')
ax.set_ylabel('λ (A)')
ax.set_title('λ = f(θ)')
ax.legend()
ax.set_xlim(left=26)  # x ekseni sıfırdan başlar
ax.set_ylim(bottom=0)  # y ekseni sıfırdan başlar
plt.show()

