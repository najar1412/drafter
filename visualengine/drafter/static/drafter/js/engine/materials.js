// base materials
var m_hy = new THREE.MeshStandardMaterial({
    color: 0x6AD4EB,
    roughness: 0,
    metalness: .2,
    flatShading: true
});

var m_context = new THREE.MeshStandardMaterial({
    color: 0xE2E2E2,
    roughness: .1,
    metalness: .2,
    flatShading: true
});

var m_land = new THREE.MeshStandardMaterial({
    color: 0xc7c7c7,
    roughness: .9,
    metalness: 0,
    flatShading: true
});



var defaultGlass = new THREE.MeshPhysicalMaterial( {
    color: 0xC0C0C0,
    metalness: 1,
    roughness: .8,
    opacity: 0.8,
    transparent: true,
    envMapIntensity: 2,
    flatShading: true
    // TODO: Add custom blend mode that modulates background color by this materials color.
} );

var defaultSteel = new THREE.MeshPhysicalMaterial ({
    shininess: 15,
    color: 0xf0f0f0,
    metal: true

});

var defaultRubber = new THREE.MeshPhysicalMaterial ({
    color: 0x000000,
    metalness: 0.5,
    roughtness: 0.3
});

var defaultSteelBlack = new THREE.MeshPhysicalMaterial ({
    color: 0x000000,
    metalness: 0.5,
    roughness: 0.5,
    shininess: 15,

});