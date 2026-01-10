import json

import pdal


def filter_by_incidence(input: str, output: str, max_angle: float = 15.0):
    pipeline_def = {
        "pipeline": [
            input,
            {
                "type": "filters.expression",
                "expression": f"abs(ScanAngleRank <= {max_angle})",
            },
            {
                "type": "writers/las",
                "filename": output,
            },
        ]
    }

    pipeline = pdal.Pipeline(json.dumps(pipeline_def))
    count = pipeline.execute()
    print(f"Filtered {count} points.")
