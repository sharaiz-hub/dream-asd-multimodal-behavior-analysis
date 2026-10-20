import os
import random
import numpy as np
import torch
import yaml
import json
import logging
from pathlib import Path
from datetime import datetime


def load_config(config_path: str = "configs/config.yaml") -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ["PYTHONHASHSEED"] = str(seed)
    print(f"[seed] All seeds set to {seed}")


def get_device(cfg: dict) -> torch.device:
    device_str = cfg["project"]["device"]
    if device_str == "cuda" and not torch.cuda.is_available():
        print("[WARNING] CUDA requested but not available. Falling back to CPU.")
        return torch.device("cpu")
    device = torch.device(device_str)
    name = torch.cuda.get_device_name(0) if device.type == "cuda" else "CPU"
    print(f"[device] Using: {device} ({name})")
    return device


def setup_logger(name: str, log_dir: str, experiment_id: str) -> logging.Logger:
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = os.path.join(log_dir, f"{experiment_id}.log")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


def get_experiment_id(model_name: str) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{model_name}_{ts}"


def save_results(results: dict, save_path: str) -> None:
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[results] Saved to {save_path}")


def count_parameters(model: torch.nn.Module) -> int:
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"[model] Total params: {total:,} | Trainable: {trainable:,}")
    return trainable
