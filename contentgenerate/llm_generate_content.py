from contentgenerate import Industry_segmentation_search
from contentgenerate import industry_segmentation_anaylsis

from contentgenerate import segmented_products_search
from contentgenerate import segmented_products_anaysis

from contentgenerate import competitive_product_analysis

from contentgenerate import screenplay_product_characteristic
from contentgenerate import screenplay_generate

from contentgenerate import screenplay_hot_movie

from contentgenerate import screenplay_outputparser

from contentgenerate import customer_profiling_analysis

from contentgenerate import screenplay_cusomer_profiling
def get_segmentation_anaysis(industry,enterprise_name,enterprise_industry_introduction):
    try:
        segmentation_description=Industry_segmentation_search.get_industry_segmentation_search(industry)
        res=industry_segmentation_anaylsis.get_industry_segmentation_anaysis(enterprise_name,enterprise_industry_introduction,segmentation_description)
        return res
    except Exception as e:
        return f"Error: {e}"
def get_product_anaysis(industry,segmentation,enterprise_name,enterprise_industry_introduction):
    try:
        segmentation_description=segmented_products_search.get_segmentation_product_search(industry,segmentation)
        res=segmented_products_anaysis.get_segmentation_prodcut_anaysis(enterprise_name,enterprise_industry_introduction,segmentation_description)
        return res
    except Exception as e:
        return f"Error: {e}"

def get_competitive_anaysis(enterprise_name,product_name,product_description):
    try:
        res=competitive_product_analysis.get_industry_segmentation_anaysis(enterprise_name,product_name,product_description)
        return res
    except Exception as e:
        return f"Error: {e}"

def get_srennplay_plot(enterprise_name,competitive_anaysis):
    try:
        characterisitc=screenplay_product_characteristic.get_product_characterisitc(competitive_anaysis)
        res=screenplay_generate.get_screenplay_plot(enterprise_name,characterisitc)
        return res
    except Exception as e:
        return f"Error: {e}"
    
def get_movie_to_screenplay(filepath,topic):
    try:
        res=screenplay_hot_movie.get_movie_to_screenplay(filepath,topic)
        res=screenplay_outputparser.get_screenplay_output(res)
        return res
    except Exception as e:
        return f"Error: {e}"
    
def get_custom_profiling_anaysis(product_name,product_description):
    try:
        res=customer_profiling_analysis.get_custom_profiling_anaysis(product_name,product_description)
        return res
    except Exception as e:
        return f"Error: {e}"
    
def get_customer_profiling_to_screenplot(enterprise_name,customer_profiling):
    try:
        res=screenplay_cusomer_profiling.get_custmer_profiling_to_screenplay(enterprise_name,customer_profiling)
        return res
    except Exception as e:
        return f"Error: {e}"
