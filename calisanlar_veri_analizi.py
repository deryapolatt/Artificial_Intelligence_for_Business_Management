import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("e__train.csv")

# Yaş aralıklarını tanımla
age_ranges = [(20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65)]

attrition_ratios = []
for age_range in age_ranges:
    age_min, age_max = age_range
    attrition_age_range = df[(df['Age'] >= age_min) & (df['Age'] < age_max)]
    attrition_count = attrition_age_range['Attrition'].value_counts()

    attrition_ratio = 0
    if 'Yes' in attrition_count:
        attrition_ratio = attrition_count['Yes'] / attrition_count.sum()

    attrition_ratios.append(attrition_ratio)

age_labels = ['{}-{}'.format(age_range[0], age_range[1]) for age_range in age_ranges]
plt.bar(age_labels, attrition_ratios)
plt.xlabel('Yaş Aralığı')
plt.ylabel('Attrition Oranı')
plt.title('Yaş Aralığına Göre Attrition Oranları')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Yaş aralıklarını tanımla
age_ranges = [(20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65)]

# Yaş aralığına göre gruplayarak Attrition değerlerini say ve oranı hesapla
attrition_ratios = []
for age_range in age_ranges:
    age_min, age_max = age_range
    attrition_age_range = df[(df['Age'] >= age_min) & (df['Age'] < age_max)]
    attrition_count = attrition_age_range['Attrition'].value_counts()

    attrition_ratio = 0
    if 'Yes' in attrition_count:
        attrition_ratio = attrition_count['Yes'] / attrition_count.sum()

    attrition_ratios.append(attrition_ratio)

age_labels = ['{}-{}'.format(age_range[0], age_range[1]) for age_range in age_ranges]
plt.bar(age_labels, attrition_ratios)
plt.xlabel('Yaş Aralığı')
plt.ylabel('Attrition Oranı')
plt.title('Yaş Aralığına Göre Attrition Oranları')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# BusinessTravel değişkenine göre Attrition oranlarını hesapla
attrition_by_travel = df[df['Attrition'] == 'Yes']['BusinessTravel'].value_counts(normalize=True)

attrition_by_travel.plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.axis('equal')
plt.title('Business Travel Türüne Göre Attrition Oranları')
plt.ylabel('')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# DailyRate'i belirli aralıklara bölündü
bin_labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500+']
df['DailyRateRange'] = pd.cut(df['DailyRate'], bins=[0, 500, 1000, 1500, 2000, 2500, float('inf')], labels=bin_labels,
                              right=False)

attrition_by_rate = df[df['Attrition'] == 'Yes']['DailyRateRange'].value_counts(normalize=True)

attrition_by_rate.plot(kind='bar')
plt.xlabel('DailyRate Aralığı')
plt.ylabel('Attrition Oranı')
plt.title('DailyRate Aralığına Göre Attrition Oranları')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Department değişkenine göre Attrition oranlarını hesapla
attrition_by_department = df[df['Attrition'] == 'Yes']['Department'].value_counts(normalize=True)

attrition_by_department.plot(kind='bar')
plt.xlabel('Departman')
plt.ylabel('Attrition Oranı')
plt.title('Departmanlara Göre Attrition Oranları')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# DistanceFromHome değişkenine göre Attrition oranlarını hesapla
attrition_by_distance = df[df['Attrition'] == 'Yes']['DistanceFromHome'].value_counts(normalize=True)

attrition_by_distance.plot(kind='bar')
plt.xlabel('Evden Uzaklık')
plt.ylabel('Attrition Oranı')
plt.title('Evden Uzaklığa Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# EducationField değişkenine göre Attrition oranlarını hesapla
attrition_by_education_field = df[df['Attrition'] == 'Yes']['EducationField'].value_counts(normalize=True)

attrition_by_education_field.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Eğitim Alanına Göre Attrition Oranları')
plt.ylabel('')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# StockOptionLevel değişkenine göre Attrition oranlarını hesapla
attrition_by_stock_option = df[df['Attrition'] == 'Yes']['StockOptionLevel'].value_counts(normalize=True)

attrition_by_stock_option.plot(kind='bar')
plt.xlabel('Hisse Senedi Seviyesi')
plt.ylabel('Attrition Oranı')
plt.title('Hisse Senedi Seviyesine Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# TotalWorkingYears değişkenine göre Attrition oranlarını hesapla ve sırala
attrition_by_working_years = df[df['Attrition'] == 'Yes']['TotalWorkingYears'].value_counts(normalize=True).sort_index()

attrition_by_working_years.plot(kind='bar')
plt.xlabel('Toplam Çalışma Yılı')
plt.ylabel('Attrition Oranı')
plt.title('Toplam Çalışma Yılına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# TrainingTimesLastYear değişkenine göre Attrition oranlarını hesapla
attrition_by_training_times = df[df['Attrition'] == 'Yes'].groupby('TrainingTimesLastYear').size() / df.groupby(
    'TrainingTimesLastYear').size()

attrition_by_training_times.plot(kind='bar')
plt.xlabel('Eğitim Süresi (Geçen Yıl)')
plt.ylabel('Attrition Oranı')
plt.title('Eğitim Süresine Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# WorkLifeBalance değişkenine göre Attrition oranlarını hesapla
attrition_by_worklife = df[df['Attrition'] == 'Yes']['WorkLifeBalance'].value_counts(normalize=True)

attrition_by_worklife.plot(kind='bar')
plt.xlabel('İş & Yaşam Dengesi')
plt.ylabel('Attrition Oranı')
plt.title('İş & Yaşam Dengesine Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# YearsAtCompany değişkenine göre Attrition oranlarını hesapla
attrition_by_years = df[df['Attrition'] == 'Yes']['YearsAtCompany'].value_counts(normalize=True)

attrition_by_years = attrition_by_years.sort_index()

attrition_by_years.plot(kind='bar')
plt.xlabel('Şirkette Geçen Yıl Sayısı')
plt.ylabel('Attrition Oranı')
plt.title('Şirkette Geçen Yıl Sayısına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# YearsInCurrentRole değişkenine göre Attrition oranlarını hesapla
attrition_by_years_in_role = df[df['Attrition'] == 'Yes']['YearsInCurrentRole'].value_counts(normalize=True)

attrition_by_years_in_role = attrition_by_years_in_role.sort_index()

attrition_by_years_in_role.plot(kind='bar')
plt.xlabel('Mevcut Rolde Geçen Yıl Sayısı')
plt.ylabel('Attrition Oranı')
plt.title('Mevcut Rolde Geçen Yıl Sayısına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# YearsSinceLastPromotion değişkenine göre Attrition oranlarını hesapla
attrition_by_years_since_promotion = df[df['Attrition'] == 'Yes']['YearsSinceLastPromotion'].value_counts(
    normalize=True)

attrition_by_years_since_promotion = attrition_by_years_since_promotion.sort_index()

attrition_by_years_since_promotion.plot(kind='bar')
plt.xlabel('Son Terfi Tarihinden Geçen Yıl Sayısı')
plt.ylabel('Attrition Oranı')
plt.title('Son Terfi Tarihinden Geçen Yıl Sayısına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# YearsWithCurrManager değişkenine göre Attrition oranlarını hesapla
attrition_by_years_with_manager = df[df['Attrition'] == 'Yes']['YearsWithCurrManager'].value_counts(normalize=True)

attrition_by_years_with_manager = attrition_by_years_with_manager.sort_index()

attrition_by_years_with_manager.plot(kind='bar')
plt.xlabel('Mevcut Yöneticiyle Geçen Yıl Sayısı')
plt.ylabel('Attrition Oranı')
plt.title('Mevcut Yöneticiyle Geçen Yıl Sayısına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# DailyRateRange değişkenine göre Attrition oranlarını hesapla
attrition_by_daily_rate = df[df['Attrition'] == 'Yes']['DailyRateRange'].value_counts(normalize=True)

attrition_by_daily_rate = attrition_by_daily_rate.sort_index()

attrition_by_daily_rate.plot(kind='bar')
plt.xlabel('Günlük Ücret Aralığı')
plt.ylabel('Attrition Oranı')
plt.title('Günlük Ücret Aralığına Göre Attrition Oranları')
plt.xticks(rotation=0)
plt.show()

#TAMAMINI GÖRÜNTÜLEMEK İÇİN

import pandas as pd
import matplotlib.pyplot as plt

# Değişkenlerin listesi
variables = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',
             'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole',
             'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime',
             'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
             'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
             'YearsSinceLastPromotion', 'YearsWithCurrManager', 'DailyRateRange']

for variable in variables:
    attrition_by_variable = df[df['Attrition'] == 'Yes'][variable].value_counts(normalize=True)
    attrition_by_variable.plot(kind='bar')
    plt.xlabel(variable)
    plt.ylabel('Attrition Oranı')
    plt.title(f'{variable} Değişkenine Göre Attrition Oranları')
    plt.xticks(rotation=45)
    plt.show()
