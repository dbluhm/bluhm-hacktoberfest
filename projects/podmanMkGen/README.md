# Podman Container Makefile Generator

**Usage:** `mkgen -f CONFIG_FILE.toml`

### Configuration file options

An example configuration file might look something like:

```toml
[pod.base]
name = "base"

[pod.other]
name = "other"

[container.nextcloud]
name = "nextcloud"
image = "nextcloud"
pod = "base"
ports = [
    "8080:80",
    "443:443"
]
volumes = [
    "/srv/nextcloud:/var/www/html:z",
    "/mnt/storage/nextcloud-data:/var/www/html/data:z"
]
```

This will produce a hash that looks something like this (as JSON):
```json
{
    "pod": {
        "base": {
            "name": "base"
        },
        "other": {
            "name": "other"
        }
    },
    "container": {
        "nextcloud": {
            "name": "nextcloud",
            "image": "nextcloud",
            "pod": "base",
            "ports": [
                "8080:80",
                "443:443"
            ],
            "volumes": [
                "/srv/nextcloud:/var/www/html:z",
                "/mnt/storage/nextcloud-data:/var/www/html/data:z"
            ]
        }
    }
}
```

### Template Parameters

The template expects the following values for its context (expressed as JSON but
should be passed as a hash):

```json
{
    "pods": [
        {
            "name": "base",
            "containers": [
                {
                    "name": "nextcloud",
                    "ports": ["8080:80", "443:443"]
                }
            ]
        }
    ],
    "containers": [
        {
            "name": "nextcloud",
            "image": "nextcloud",
            "pod": "base",
            "ports": ["8080:80", "443:443"],
            "volumes": [
                "/srv/nextcloud:/var/www/html:z",
                "/mnt/storage/nextcloud-data:/var/www/html/data:z"
            ]
        }
    ]
}
```

### Mapping from config to template Parameters

As there is obviously a difference between the hash taken in from the config and
the hash we need to pass to the template, some processing is required.

The `pod` hash should be mapped to an array with the containers attribute being
populated by filtering a list of containers on their `pod` attribute.

The `container` hash should likewise be flattened from a hash to an array.
