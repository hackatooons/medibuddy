from pydantic import BaseModel


class HeartPatient(BaseModel):
    age: int
    anaemia: int
    creatinine_phosphokinase: float
    diabetes: int
    ejection_fraction: float
    high_blood_pressure: int
    platelets: int
    serum_creatinine: float
    serum_sodium: float
    sex: int
    smoking: int
    time: int


class BreastCancerPatient(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float