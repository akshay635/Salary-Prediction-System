# -*- coding: utf-8 -*-

import streamlit as st
import joblib as jb
import importlib
import src.config as config

importlib.reload(config)

@st.cache_resource
def load_model():
    
    model = jb.load(config.MODEL_PATH)
    
    preprocessor = jb.load(config.ENCODER_PATH)
    
    return model, preprocessor