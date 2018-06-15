// Env
var CUBECAMERA = new THREE.CubeCamera(1, 20000, 256);
CUBECAMERA.renderTarget.texture.minFilter = THREE.LinearMipMapLinearFilter;

// textures
var TEXTURE = new THREE.TextureLoader();

var textureConcrete = TEXTURE.load( "/static/drafter/js/engine/assets/concrete.jpg", function ( texture ) {

    texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
    texture.offset.set( 0, 0 );
    texture.repeat.set( 100, 100 );

} );

var m_hy = new THREE.MeshStandardMaterial({
    color: 0x6AD4EB,
    roughness: 0,
    metalness: .2,
    flatShading: true
});

var m_context = new THREE.MeshStandardMaterial({
    color: 0xE2E2E2,
    roughness: 1,
    metalness: .1,
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
    opacity: 0.8,
    transparent: true,
    envMap: CUBECAMERA,
    envMapIntensity: 3,
    reflectivity: 0,
    roughness:0.6
    // TODO: Add custom blend mode that modulates background color by this materials color.
} );

var defaultSteel = new THREE.MeshPhysicalMaterial ({
    color: 0xf0f0f0

});

var defaultRubber = new THREE.MeshPhysicalMaterial ({
    color: 0x000000
});

var defaultSteelBlack = new THREE.MeshPhysicalMaterial ({
    color: 0x000000
});

var defaultConcrete = new THREE.MeshPhysicalMaterial ({
    map: textureConcrete,
    flatShading: true
    
    // specularMap: textureLoader.load( "static/textures/earth_specular_2048.jpg" ),
    // normalMap: textureLoader.load( "static/textures/earth_normal_2048.jpg" ),
    // normalScale: new THREE.Vector2( 0.85, 0.85 )
} );

var defaultGhost = new THREE.MeshPhysicalMaterial ({
    color: 0xffffff,
    opacity: 0.4,
    transparent: true,
    envMap: CUBECAMERA,
    envMapIntensity: 2,
    roughness:1
});