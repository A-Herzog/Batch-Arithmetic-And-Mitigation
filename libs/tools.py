import xml.etree.ElementTree as ET
import pandas as pd
import os
import copy


# Define the namespace for the XML elements
ET.register_namespace('', 'https://a-herzog.github.io')
ns = {'QS': 'https://a-herzog.github.io'}


def load_xml_file(file: str):
    """
    Load statistics from an XML file and return the tree and the root element.

    Args:
        file (str): Path to the XML file.

    Returns:
        tuple[ET.ElementTree[ET.Element], ET.Element]: The XML tree and its root element.
    """
    tree = ET.parse(file)

    if tree is None:
        raise ValueError(f"Failed to parse XML file: {file}")
    root = tree.getroot()
    if root is None:
        raise ValueError(f"Failed to get root element from XML tree for file: {file}")

    return tree, root


def save_xml_file(tree, file: str):
    """
    Saves and XML tree to a file.

    Args:
        tree: xml tree.
        file (str): Path to the output XML file.
    """
    with open(file, 'wb') as f:
        tree.write(f)


def get_element(root: ET.Element, path: str, file: str):
    """
    Retrieve an XML element based on the provided path.

    Args:
        root (ET.Element): The root element of the XML tree.
        path (str): The path to the desired XML element.
        file (str): File from which the xml data was loaded (for printing error messages)

    Returns:
        ET.Element: The found XML element.

    Raises:
        ValueError: If the element is not found.
    """
    el = root.find("QS:" + path, ns)
    if el is None:
        raise ValueError(f"Failed to find element '{path}' in XML file: {file}")
    return el


def get_elements(root: ET.Element, path: str, file: str):
    """
    Retrieve all XML elements based on the provided path.

    Args:
        root (ET.Element): The root element of the XML tree.
        path (str): The path to the desired XML elements.
        file (str): File from which the xml data was loaded (for printing error messages)

    Returns:
        list[ET.Element]: The found XML elements.

    Raises:
        ValueError: If the element is not found.
    """
    els = root.findall("QS:" + path, ns)
    if not els:
        raise ValueError(f"Failed to find element '{path}' in XML file: {file}")
    return els


def get_or_add_element(root: ET.Element, path: str):
    """
    Retrieve an XML element based on the provided path.
    Adds the element, if its not existing.

    Args:
        root (ET.Element): The root element of the XML tree.
        path (str): The path to the desired XML element.

    Returns:
        ET.Element: The found XML element.

    Raises:
        ValueError: If the element is not found.
    """
    el = root.find("QS:" + path, ns)
    if el is None:
        el = ET.Element(path)
        root.append(el)
    return el


def prepare_statistics(c_needed: int, useRecord=None) -> list:
    data = []
    for file in os.listdir('Statistics'):
        if not file.endswith('.xml'):
            continue
        info = {"mode": "", "S": "", "model_rho": 0, "model_CV[S]": 1, "c": c_needed, "b_min": 0, "b_max": 0, "bI": 1, "time": -1, "name": "", "name_short": "", "file": "Statistics" + os.sep + file}
        file = file[:-4]

        is_range = False
        is_time_last = False
        is_time_max = False
        is_compare = False
        is_multirun = False
        for part in file.split('-'):
            if part == "Range":
                is_range = True
                continue
            if part == "Time":
                is_time_last = True
                continue
            if part == "TimeMax":
                is_time_max = True
                continue
            if part == "Compare":
                is_compare = True
                continue
            if part.startswith("run"):
                is_multirun = True
                info["run"] = int(part[3:])
            if part == "exp":
                info["S"] = "Exp"
                continue
            if part == "log":
                info["S"] = "Log"
                continue
            if part.startswith("rho"):
                info["model_rho"] = int(part[3:]) / 100
                continue
            if part.startswith("CV"):
                info["model_CV[S]"] = float(part[2:])
                continue
            if part.startswith("bIRange"):
                info["bI"] = str(part[7:])
                continue
            if part.startswith("bI"):
                info["bI"] = int(part[2:])
                continue
            if part.startswith("bmin"):
                info["b_min"] = int(part[4:])
                continue
            if part.startswith("b"):
                info["b_max"] = int(part[1:])
                if c_needed < 1:
                    info["c"] = 1
                else:
                    info["c"] = int(c_needed / info["b_max"])
                continue
            if part.startswith("time"):
                info["time"] = int(part[4:])
                continue
        if info["b_min"] == 0:
            info["b_min"] = info["b_max"]

        if is_range:
            info["mode"] = "range"
            info["name"] = f'Service batch size range, S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_min"]}..{info["b_max"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_min"]}..{info["b_max"]}'
            if useRecord is None or useRecord(info):
                data.append(info)
            continue

        if is_time_last:
            info["mode"] = "time-last"
            info["name"] = f'Service batch with timed release (last), S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
            if useRecord is None or useRecord(info):
                data.append(info)
            continue

        if is_time_max:
            info["mode"] = "time-max"
            info["name"] = f'Service batch with timed release (max), S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
            if useRecord is None or useRecord(info):
                data.append(info)
            continue

        if is_compare:
            info["mode"] = "compare"
            info["name"] = f'Base scenario, S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c=1, bI=1, bS={info["b_max"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI=1, bS={info["b_max"]}'
            if useRecord is None or useRecord(info):
                data.append(info)
            continue

        if is_multirun:
            info["mode"] = "multirun"
            info["name"] = f'Multi run, S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_max"]}, nr={info["run"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_max"]}, nr={info["run"]}'
            if useRecord is None or useRecord(info):
                data.append(info)
            continue

        if info["time"] < 0:
            info["mode"] = "fixed"
            info["name"] = f'Base scenario, S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_max"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_max"]}'
        else:
            info["mode"] = "time"
            info["name"] = f'Base scenario, S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, c={info["c"]}, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
            info["name_short"] = f'S={info["S"]}, CV[S]={info["model_CV[S]"]}, rho={int(info["model_rho"] * 100)}%, bI={info["bI"]}, bS={info["b_max"]}, t={info["time"]}'
        if useRecord is None or useRecord(info):
            data.append(info)

    return data


def load_statistics(data: list):
    """
    Load statistics for each item in the provided data list.

    Args:
        data (list): A list of dictionaries, each containing a 'file' key with the path to the XML file.
    """
    for item in data:
        tree, root = load_xml_file(item["file"])
        item["statistics_root"] = root
        item["statistics_tree"] = tree

        # Waiting times
        el = get_element(root, 'StatisticsWaitingTimesAllClients', item['file'])
        item["E[W]"] = float(el.attrib["Mean"])
        item["Std[W]"] = float(el.attrib["StandardDeviation"])
        item["CV[W]"] = item["Std[W]"] / max(1, item["E[W]"])
        item["count"] = int(el.attrib["Count"])

        # Service times
        el = get_element(root, 'StatisticsProcessTimesAllClients', item['file'])
        item["E[S]"] = float(el.attrib["Mean"])
        item["Std[S]"] = float(el.attrib["StandardDeviation"])
        item["CV[S]"] = item["Std[S]"] / max(1, item["E[S]"])

        # Residence times
        el = get_element(root, 'StatisticsResidenceTimesAllClients', item['file'])
        item["E[V]"] = float(el.attrib["Mean"])
        item["Std[V]"] = float(el.attrib["StandardDeviation"])
        item["CV[V]"] = item["Std[V]"] / max(1, item["E[V]"])

        # Customers in system
        el = get_element(root, 'StatisticsClientsInSystem', item['file'])
        item["E[N]"] = float(el.attrib["Mean"])
        item["Std[N]"] = float(el.attrib["StandardDeviation"])
        item["CV[N]"] = item["Std[N]"] / max(1, item["E[N]"])

        # Customers in queue
        el = get_element(root, 'StatisticsClientsInSystemAllQueues', item['file'])
        item["E[NQ]"] = float(el.attrib["Mean"])
        item["Std[NQ]"] = float(el.attrib["StandardDeviation"])
        item["CV[NQ]"] = item["Std[NQ]"] / max(1, item["E[NQ]"])

        # Utilization Rho
        el = get_element(root, 'StatisticsUtilizationRhoAll', item['file'])
        item["rho"] = float(el.attrib["Value"])

        # Batch size statistics
        el = get_element(root, 'StatisticsClientsAtStationProcess', item['file'])
        el2 = get_element(el, 'StationData', item['file'])
        assert el2.text is not None
        batch_sizes = el2.text.split(';')
        batch_sizes.pop(0)  # Remove empty time entry
        batch_sizes = [float(rec) for rec in batch_sizes]
        batch_sizes_time_sum = sum(batch_sizes)
        batch_sizes = [rec / batch_sizes_time_sum for rec in batch_sizes]
        item["batch_sizes"] = batch_sizes


def build_df(data):
    data2 = [copy.deepcopy(item) for item in data]
    for item in data2:
        del item["file"]
        del item["statistics_root"]
        del item["statistics_tree"]

    return pd.DataFrame(data2)


def find_same_with_other_b(data: list[dict], base_rec: dict, bI: int | str | None, bS_min: int | None, bS_max: int | None, time: int | None) -> dict:
    for rec in data:
        if rec["mode"] != base_rec["mode"] or rec["S"] != base_rec["S"] or rec["model_rho"] != base_rec["model_rho"] or rec["model_CV[S]"] != base_rec["model_CV[S]"]:
            continue

        if time is not None:
            if rec["time"] != time:
                continue

        if bI is None:
            if rec["bI"] != base_rec["bI"]:
                continue
        else:
            if rec["bI"] != bI:
                continue

        if bS_min is None:
            if rec["b_min"] != base_rec["b_min"]:
                continue
        else:
            if rec["b_min"] != bS_min:
                continue

        if bS_max is None:
            if rec["b_max"] != base_rec["b_max"]:
                continue
        else:
            if rec["b_max"] != bS_max:
                continue
        return rec

    raise ValueError("Record not found")
