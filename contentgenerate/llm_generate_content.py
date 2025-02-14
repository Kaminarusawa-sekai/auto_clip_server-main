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

from contentgenerate import screenplay_to_screenplay

from contentgenerate import market_paln_base
from contentgenerate import screenplay_program_generator_redbook
from contentgenerate import screenplay_program_generator_douyin
from contentgenerate import screenplay_generator_from_materials
from contentgenerate import screenplay_generator_add_extra
from contentgenerate import screenplay_yamltoJson
from contentgenerate import yaml_repair

import random



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
        res=competitive_product_analysis.get_competitive_product_anaysis(enterprise_name,product_name,product_description)
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

def get_screenplay_to_screenplay(screenplay):
    try:
        res=screenplay_to_screenplay.get_screenplay_to_screenplay(screenplay)
        return res
    except Exception as e:
        return f"Error: {e}"
    

def get_market_plan(enterprise_name,product_name,product_description):
    try:
        custom_profiling=customer_profiling_analysis.get_custom_profiling_anaysis(product_name,product_description)
        competitive_anaysis=competitive_product_analysis.get_competitive_product_anaysis(enterprise_name,product_name)
        product_characteristic=screenplay_product_characteristic.get_product_characterisitc(competitive_anaysis)
        market_plan=market_paln_base.get_market_plan(enterprise_name,product_name,competitive_anaysis,custom_profiling,product_characteristic)
        return market_plan
    except Exception as e:
        return f"Error: {e}"




def get_auto_screenplay(enterprise_name,product_name,product_description,market_plan,hot_points:list,hot_starts:list,video_descriptions:dict,voices:list,BGMS:list,fonts:list,yaml_filepath_redbook,yaml_filepath_douyin):
    try:
        hot_point=random.choice(hot_points)
        hot_start=random.choice(hot_starts)
        screenplay_redbook=screenplay_program_generator_redbook.get_screenplay_redbook(market_plan,hot_point,hot_start)
        screenplay_douyin=screenplay_program_generator_douyin.get_screenplay_douyin(market_plan,hot_point,hot_start)
        get_yaml_screenplay(screenplay_redbook,video_descriptions,voices,BGMS,fonts,yaml_filepath_redbook)
        get_yaml_screenplay(screenplay_douyin,video_descriptions,voices,BGMS,fonts,yaml_filepath_douyin)
    except Exception as e:
        return f"Error: {e}"



def get_yaml_screenplay(screenplay_original,video_descriptions:dict,voices:list,BGMS:list,fonts:list,yaml_filepath):
    materials=""
    for k in video_descriptions.keys():
        materials=materials+"素材名："+k+",描述："+video_descriptions[k]
    voice="配音库："
    i=0
    for v in voices:
        voice=voice+"("+i+")"+v
        i=i+1
    
    i=0
    bGM="BGM库："
    for b in BGMS:
        bGM=bGM+"("+i+")"+v
        i=i+1
    
    i=0
    font="字体库："
    for f in fonts:
        font=font+"("+i+")"+f
        i=i+1

    
        

    screenplay_material=screenplay_generator_from_materials.get_screenplay_from_materials(screenplay_original,materials)
    screenplay_ectra=screenplay_generator_add_extra.get_screenplay_add_extra(screenplay_material,voice,bGM,font)
    screenplay_output=screenplay_outputparser.get_screenplay_out(screenplay_ectra)
    json_text=screenplay_yamltoJson.get_screenplay_yamltojson(screenplay_output)
    yaml_repair.repaire_yaml(json_text,yaml_filepath)







